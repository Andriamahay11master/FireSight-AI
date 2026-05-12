# backend/app/services/inference_service.py

from ultralytics import YOLO
from PIL import Image
import io
from app.utils.image_processing import preprocess_image
from app.core.config import settings
from app.services.risk_engine import compute_risk_level
from app.core.logger import get_logger

logger = get_logger(__name__)

logger.info("Loading YOLO model...")

# -----------------------------------------
# LOAD MODEL ONCE
# -----------------------------------------
model = YOLO(settings.MODEL_WEIGHTS_PATH)

# -----------------------------------------
# RUN INFERENCE
# -----------------------------------------
def run_inference(image_bytes: bytes):

    # Convert bytes → PIL image
    image = preprocess_image(image_bytes)

    # Run YOLO inference
    results = model(image)

    detections = []

    # Process detections
    for result in results:

        boxes = result.boxes

        for box in boxes:

            # Coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Confidence
            confidence = float(box.conf[0])

            # Class ID
            class_id = int(box.cls[0])

            # Label
            label = model.names[class_id]

            detections.append({
                "label": label,
                "confidence": round(confidence, 2),
                "bounding_box": {
                    "x": int(x1),
                    "y": int(y1),
                    "width": int(x2 - x1),
                    "height": int(y2 - y1)
                }
            })

    risk_level = compute_risk_level(detections)

    return {
        "detections": detections,
        "risk_level": risk_level
    }