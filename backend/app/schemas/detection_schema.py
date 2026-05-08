# backend/app/schemas/detection_schema.py

from pydantic import BaseModel
from typing import List


# -----------------------------------------
# Bounding Box Schema
# -----------------------------------------
class BoundingBox(BaseModel):
    x: int
    y: int
    width: int
    height: int


# -----------------------------------------
# Detection Schema
# -----------------------------------------
class Detection(BaseModel):
    label: str
    confidence: float
    bounding_box: BoundingBox


# -----------------------------------------
# Detection Response Schema
# -----------------------------------------
class DetectionResponse(BaseModel):
    success: bool
    filename: str
    detections: List[Detection]
    risk_level: str
    message: str