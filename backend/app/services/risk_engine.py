# backend/app/services/risk_engine.py

from enum import Enum


# -----------------------------------------
# Risk Level Enumeration
# -----------------------------------------
class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


# -----------------------------------------
# Compute Risk Level
# -----------------------------------------
def compute_risk_level(detections: list[dict]) -> str:
    """
    Compute fire risk level based on detected objects.

    Rules (V1):
    - Fire + Smoke detected       -> HIGH
    - Fire only detected          -> MEDIUM
    - Smoke only detected         -> LOW
    - No detections               -> LOW
    """

    labels = [d["label"].lower() for d in detections]

    has_fire = "fire" in labels
    has_smoke = "smoke" in labels

    if has_fire and has_smoke:
        return RiskLevel.HIGH.value

    if has_fire:
        return RiskLevel.MEDIUM.value

    return RiskLevel.LOW.value