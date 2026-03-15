"""
@file test_job_store.py
@description Tests for the in-memory job store.
"""

from data_loader.job_store import JobStore


class TestJobStore:
    def test_create_returns_uuid(self):
        """It should create a job and return a UUID4 string."""
        store = JobStore()
        job_id = store.create("single")
        assert isinstance(job_id, str)
        assert len(job_id) == 36  # UUID4 format: 8-4-4-4-12

    def test_get_returns_job(self):
        """It should retrieve a created job by ID."""
        store = JobStore()
        job_id = store.create("batch")
        job = store.get(job_id)
        assert job is not None
        assert job["job_id"] == job_id
        assert job["status"] == "pending"
        assert job["job_type"] == "batch"
        assert job["result"] is None
        assert job["error"] is None
        assert job["created_at"] is not None
        assert job["completed_at"] is None

    def test_get_missing_returns_none(self):
        """It should return None for non-existent job IDs."""
        store = JobStore()
        assert store.get("non-existent-id") is None

    def test_update_status(self):
        """It should update job status."""
        store = JobStore()
        job_id = store.create("single")
        store.update(job_id, status="running")
        job = store.get(job_id)
        assert job["status"] == "running"

    def test_update_result(self):
        """It should update job result and completed_at."""
        store = JobStore()
        job_id = store.create("single")
        store.update(job_id, status="completed", result={"processed": 1})
        job = store.get(job_id)
        assert job["status"] == "completed"
        assert job["result"] == {"processed": 1}
        assert job["completed_at"] is not None

    def test_update_error(self):
        """It should update job error."""
        store = JobStore()
        job_id = store.create("single")
        store.update(job_id, status="failed", error="Something went wrong")
        job = store.get(job_id)
        assert job["status"] == "failed"
        assert job["error"] == "Something went wrong"

    def test_update_missing_is_noop(self):
        """It should silently ignore updates to non-existent jobs."""
        store = JobStore()
        store.update("non-existent", status="running")  # should not raise
