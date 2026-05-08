# backend/app/api/routes/health.py

from fastapi import APIRouter
from datetime import datetime

from app.schemas.response_schema import HealthResponse

router = APIRouter()

# -----------------------------------------
# Health Check Endpoint
# -----------------------------------------
@router.get("/", response_model=HealthResponse)
def health_check():
    """
    Simple API health check.
    """

    return HealthResponse(
        status="healthy",
        service="FireSight AI API",
        version="1.0.0",
        timestamp=datetime.utcnow().isoformat()
    )