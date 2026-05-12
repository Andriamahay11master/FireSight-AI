# backend/app/api/routes/alerts.py

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

# Temporary in-memory storage
alerts_store = []


@router.get("/")
def get_alerts():
    """
    Return all recorded alerts.
    """
    return {
        "success": True,
        "count": len(alerts_store),
        "alerts": alerts_store,
    }


@router.post("/")
def create_alert():
    """
    Create a mock alert (V1 placeholder).
    """

    alert = {
        "id": len(alerts_store) + 1,
        "risk_level": "HIGH",
        "message": "Fire detected - immediate attention required",
        "timestamp": datetime.utcnow().isoformat(),
        "acknowledged": False,
    }

    alerts_store.append(alert)

    return {
        "success": True,
        "message": "Alert created successfully",
        "alert": alert,
    }