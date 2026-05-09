from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

#import routes
from app.api.routes import detection, health, alerts

#app Instance
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# -----------------------------
# CORS Middleware (Frontend connection)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# -----------------------------
# Include API Routes
# -----------------------------
app.include_router(health.router, prefix="/api/health", tags=["Health"])
app.include_router(detection.router, prefix="/api/detection", tags=["Detection"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "🔥 FireSight AI API is running",
        "version": "1.0.0"
    }