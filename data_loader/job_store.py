"""
@file job_store.py
@description In-memory job tracking for the API service.
"""

import uuid
from datetime import datetime, timezone


class JobStore:
    """In-memory job store — tracks async processing jobs.

    Jobs are lost on server restart. JSON files on disk are the durable record.
    """

    def __init__(self) -> None:
        self._jobs: dict[str, dict] = {}

    def create(self, job_type: str) -> str:
        """Create a new job. Returns the UUID4 job_id."""
        job_id = str(uuid.uuid4())
        self._jobs[job_id] = {
            "job_id": job_id,
            "job_type": job_type,
            "status": "pending",
            "result": None,
            "error": None,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "completed_at": None,
        }
        return job_id

    def get(self, job_id: str) -> dict | None:
        """Get job status. Returns None if not found."""
        return self._jobs.get(job_id)

    def update(self, job_id: str, **kwargs) -> None:
        """Update job fields: status, result, error, completed_at."""
        job = self._jobs.get(job_id)
        if job is None:
            return

        for key, value in kwargs.items():
            if key in job:
                job[key] = value

        # Auto-set completed_at when status becomes terminal
        if kwargs.get("status") in ("completed", "failed") and job["completed_at"] is None:
            job["completed_at"] = datetime.now(timezone.utc).isoformat()
