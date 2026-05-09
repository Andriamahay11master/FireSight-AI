# backend/app/services/inference_service.py

from ultralytics import YOLO
from PIL import Image
import io
from app.utils.image_processing import preprocess_image

# -----------------------------------------
# LOAD MODEL ONCE
# -----------------------------------------
model = YOLO("../model/weights/best.pt")

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

    # Compute risk
    risk_level = compute_risk_level(detections)

    return {
        "detections": detections,
        "risk_level": risk_level
    }


# -----------------------------------------
# SIMPLE RISK ENGINE
# -----------------------------------------
def compute_risk_level(detections):

    fire_count = sum(
        1 for d in detections if d["label"].lower() == "fire"
    )

    smoke_count = sum(
        1 for d in detections if d["label"].lower() == "smoke"
    )

    # Basic logic
    if fire_count >= 1 and smoke_count >= 1:
        return "HIGH"

    elif fire_count >= 1:
        return "MEDIUM"

    return "LOW"