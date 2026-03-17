"""
@file api.py
@description FastAPI service for the data loader with async job queue.
"""

import asyncio
import json
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from data_loader.config import PROCESSED_DIR, sanitize_arxiv_id
from data_loader.job_store import JobStore
from data_loader.sdk import load_paper, load_papers

logger = logging.getLogger("data_loader")

app = FastAPI(title="Theo-Fish Data Loader", version="0.1.0")
job_store = JobStore()


# --- Request models ---


class SinglePaperRequest(BaseModel):
    """Request body for POST /papers."""

    arxiv_id: str
    force: bool = False


class BatchPaperRequest(BaseModel):
    """Request body for POST /papers/batch."""

    arxiv_ids: list[str]
    force: bool = False


# --- Background task runners ---


async def _run_single_paper_job(job_id: str, arxiv_id: str, force: bool) -> None:
    """Background task that processes a single paper and updates the job store."""
    job_store.update(job_id, status="running")
    try:
        result = await load_paper(arxiv_id, force=force)
        job_store.update(
            job_id,
            status="completed",
            result=result.model_dump(),
        )
    except Exception as e:
        job_store.update(
            job_id,
            status="failed",
            error=str(e),
        )


async def _run_batch_paper_job(
    job_id: str,
    arxiv_ids: list[str],
    force: bool,
) -> None:
    """Background task that processes a batch of papers and updates the job store."""
    job_store.update(job_id, status="running")
    try:
        result = await load_papers(arxiv_ids, force=force)
        job_store.update(
            job_id,
            status="completed",
            result=result.model_dump(),
        )
    except Exception as e:
        job_store.update(
            job_id,
            status="failed",
            error=str(e),
        )


# --- Endpoints ---


@app.post("/papers", status_code=202)
async def submit_paper(request: SinglePaperRequest) -> dict:
    """Submit a single paper for processing.

    Returns a job ID for polling status via GET /jobs/{job_id}.
    """
    job_id = job_store.create("single")
    asyncio.create_task(_run_single_paper_job(job_id, request.arxiv_id, request.force))
    return {"job_id": job_id, "status": "pending"}


@app.post("/papers/batch", status_code=202)
async def submit_batch(request: BatchPaperRequest) -> dict:
    """Submit a batch of papers for processing.

    Returns a job ID for polling status via GET /jobs/{job_id}.
    """
    job_id = job_store.create("batch")
    asyncio.create_task(_run_batch_paper_job(job_id, request.arxiv_ids, request.force))
    return {"job_id": job_id, "status": "pending"}


@app.get("/jobs/{job_id}")
async def get_job(job_id: str) -> dict:
    """Get the status of a processing job."""
    job = job_store.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@app.get("/papers/{arxiv_id}")
async def get_paper(arxiv_id: str) -> dict:
    """Read a processed paper's JSON from disk."""
    json_file = PROCESSED_DIR / f"{sanitize_arxiv_id(arxiv_id)}.json"
    if not json_file.exists():
        raise HTTPException(status_code=404, detail="Paper not found")

    return json.loads(json_file.read_text(encoding="utf-8"))


@app.get("/health")
async def health() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
