from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from datetime import datetime

router = APIRouter()

# -----------------------------------------
# Alerts Endpoint
# -----------------------------------------
@router.get("/")
def alerts_check():
    """
    Simple API alert check.
    """
    return {
        "status": "alerts endpoint is working",
        "service": "FireSight AI API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }
