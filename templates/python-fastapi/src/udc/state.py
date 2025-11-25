from pydantic import BaseModel

class StateResponse(BaseModel):
    uptime_seconds: int
    status: str

