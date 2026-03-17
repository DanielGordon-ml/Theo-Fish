"""
@file test_api.py
@description Tests for the FastAPI service endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from data_loader.api import app, job_store
from data_loader.models import PaperResult, BatchResult


@pytest.fixture
def client(monkeypatch):
    """Create a FastAPI TestClient with mocked SDK."""
    # Reset job store between tests
    job_store._jobs.clear()
    return TestClient(app)


class TestHealthEndpoint:
    def test_health(self, client):
        """It should return ok status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestPostPapers:
    def test_submit_single_paper(self, client, monkeypatch):
        """It should accept a paper and return a job ID."""

        async def mock_load_paper(arxiv_id, **kwargs):
            return PaperResult(
                arxiv_id="2706.03762",
                status="processed",
                converter="arxiv2md",
            )

        monkeypatch.setattr("data_loader.api.load_paper", mock_load_paper)

        response = client.post("/papers", json={"arxiv_id": "2706.03762"})
        assert response.status_code == 202
        data = response.json()
        assert "job_id" in data
        assert data["status"] == "pending"

    def test_rejects_missing_id(self, client):
        """It should reject requests without arxiv_id."""
        response = client.post("/papers", json={})
        assert response.status_code == 422


class TestPostPapersBatch:
    def test_submit_batch(self, client, monkeypatch):
        """It should accept a batch of papers and return a job ID."""

        async def mock_load_papers(arxiv_ids, **kwargs):
            return BatchResult(
                total=2,
                processed=2,
                skipped=0,
                failed=0,
                arxiv2md=2,
                mineru=0,
                results=[
                    PaperResult(arxiv_id="2706.03762", status="processed"),
                    PaperResult(arxiv_id="1810.04805", status="processed"),
                ],
            )

        monkeypatch.setattr("data_loader.api.load_papers", mock_load_papers)

        response = client.post(
            "/papers/batch",
            json={"arxiv_ids": ["2706.03762", "1810.04805"]},
        )
        assert response.status_code == 202
        data = response.json()
        assert "job_id" in data


class TestGetJob:
    def test_get_pending_job(self, client, monkeypatch):
        """It should return pending status for a new job."""

        async def mock_load_paper(arxiv_id, **kwargs):
            return PaperResult(
                arxiv_id="2706.03762",
                status="processed",
                converter="arxiv2md",
            )

        monkeypatch.setattr("data_loader.api.load_paper", mock_load_paper)

        # Create a job first
        post_response = client.post("/papers", json={"arxiv_id": "2706.03762"})
        job_id = post_response.json()["job_id"]

        # Get job status
        response = client.get(f"/jobs/{job_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["job_id"] == job_id
        # Status could be pending, running, or completed depending on timing
        assert data["status"] in ("pending", "running", "completed")

    def test_get_missing_job(self, client):
        """It should return 404 for non-existent jobs."""
        response = client.get("/jobs/non-existent-id")
        assert response.status_code == 404


class TestGetPaper:
    def test_get_processed_paper(self, client, tmp_path, monkeypatch):
        """It should return the JSON for a processed paper."""
        monkeypatch.setattr("data_loader.api.PROCESSED_DIR", tmp_path)

        # Write a fake processed JSON file
        paper_json = '{"arxiv_id": "2706.03762", "title": "Test"}'
        (tmp_path / "2706.03762.json").write_text(paper_json)

        response = client.get("/papers/2706.03762")
        assert response.status_code == 200
        data = response.json()
        assert data["arxiv_id"] == "2706.03762"

    def test_get_missing_paper(self, client, tmp_path, monkeypatch):
        """It should return 404 for papers not on disk."""
        monkeypatch.setattr("data_loader.api.PROCESSED_DIR", tmp_path)

        response = client.get("/papers/9999.99999")
        assert response.status_code == 404
