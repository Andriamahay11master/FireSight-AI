# backend/app/schemas/response_schema.py

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    timestamp: str