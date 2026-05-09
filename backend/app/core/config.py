# backend/app/core/config.py

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


# ---------------------------------------------------
# Base directories
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[3]
MODEL_DIR = BASE_DIR / "model"
WEIGHTS_DIR = MODEL_DIR / "weights"


# ---------------------------------------------------
# Application Settings
# ---------------------------------------------------
class Settings(BaseSettings):
    # -----------------------------
    # API Metadata
    # -----------------------------
    APP_NAME: str = "FireSight AI API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "API for Fire and Smoke Detection with Risk Analysis"
    )

    # -----------------------------
    # CORS
    # -----------------------------
    ALLOWED_ORIGINS: list[str] = ["*"]

    # -----------------------------
    # Model Configuration
    # -----------------------------
    MODEL_WEIGHTS_PATH: str = str(WEIGHTS_DIR / "best.pt")
    CONFIDENCE_THRESHOLD: float = 0.25

    # -----------------------------
    # Risk Thresholds
    # -----------------------------
    HIGH_RISK_MIN_DETECTIONS: int = 2

    # -----------------------------
    # Image Processing
    # -----------------------------
    DEFAULT_IMAGE_SIZE: int = 640

    # -----------------------------
    # Environment file configuration
    # -----------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


# Singleton settings instance
settings = Settings()