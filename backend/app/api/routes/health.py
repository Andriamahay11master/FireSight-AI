# backend/app/api/routes/health.py

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

# -----------------------------------------
# Health Check Endpoint
# -----------------------------------------
@router.get("/")
def health_check():
    """
    Simple API health check.
    """

    return {
        "status": "healthy",
        "service": "FireSight AI API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }