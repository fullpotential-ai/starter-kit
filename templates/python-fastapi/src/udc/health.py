from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
    status: str
    service: str
    uptime: int
    timestamp: str = datetime.utcnow().isoformat() + "Z"

