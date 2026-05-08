# backend/app/api/routes/detection.py

from fastapi import APIRouter, UploadFile, File
from app.services.inference_service import run_inference

from app.schemas.detection_schema import DetectionResponse

router = APIRouter()

# -----------------------------
# Fire & Smoke Detection Endpoint
# -----------------------------
@router.post("/detect", response_model=DetectionResponse)
async def detect_fire(file: UploadFile = File(...)):
    """
    Upload an image and get fire/smoke detection results.
    """

    # Step 1: Read image bytes
    image_bytes = await file.read()

    # Step 2: Send to inference service
    result = run_inference(image_bytes)

    # Step 3: Return structured response
    return DetectionResponse(
        success=True,
        filename=file.filename,
        detections=result["detections"],
        risk_level=result["risk_level"],
        message="Inference completed successfully"
    )