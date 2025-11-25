from pydantic import BaseModel
from typing import List

class CapabilitiesResponse(BaseModel):
    service: str
    version: str
    features: List[str]
    dependencies: List[str]
    udc_version: str = "1.0"

