# backend/app/services/inference_service.py

import random

# ---------------------------------------------------
# TEMPORARY MOCK INFERENCE
# Replace later with YOLO / TensorFlow model
# ---------------------------------------------------

def run_inference(image_bytes: bytes):
    """
    Simulate fire/smoke detection inference.

    Args:
        image_bytes (bytes): Uploaded image bytes

    Returns:
        dict: Detection results + risk level
    """

    # -----------------------------------------
    # MOCK DETECTIONS
    # -----------------------------------------
    detections = [
        {
            "label": "fire",
            "confidence": round(random.uniform(0.80, 0.99), 2),
            "bounding_box": {
                "x": 120,
                "y": 80,
                "width": 200,
                "height": 180
            }
        },
        {
            "label": "smoke",
            "confidence": round(random.uniform(0.70, 0.95), 2),
            "bounding_box": {
                "x": 300,
                "y": 150,
                "width": 250,
                "height": 220
            }
        }
    ]

    # -----------------------------------------
    # COMPUTE RISK LEVEL
    # -----------------------------------------
    risk_level = compute_risk_level(detections)

    return {
        "detections": detections,
        "risk_level": risk_level
    }


# ---------------------------------------------------
# SIMPLE RISK ENGINE (V1)
# ---------------------------------------------------

def compute_risk_level(detections):
    """
    Compute fire risk level based on detections.
    """

    fire_count = sum(1 for d in detections if d["label"] == "fire")
    smoke_count = sum(1 for d in detections if d["label"] == "smoke")

    if fire_count >= 1 and smoke_count >= 1:
        return "HIGH"

    elif fire_count >= 1:
        return "MEDIUM"

    return "LOW"