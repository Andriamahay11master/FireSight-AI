# backend/app/api/routes/health.py

from fastapi import APIRouter
from datetime import datetime

from app.schemas.response_schema import HealthResponse
from app.core.config import settings

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
        service=settings.APP_NAME,
        version=settings.APP_VERSION,
        timestamp=datetime.utcnow().isoformat()
    )