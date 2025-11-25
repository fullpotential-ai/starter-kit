from pydantic import BaseModel
from typing import Optional, Dict, Any

class Message(BaseModel):
    type: str = "command"
    payload: Dict[str, Any]
    trace_id: Optional[str] = None

class MessageResponse(BaseModel):
    received: bool
    trace_id: Optional[str] = None

