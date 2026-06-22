from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

class LocationCreate(BaseModel):
    client_point_id: UUID
    device_id: UUID
    lat: float
    lon: float
    accuracy: float
    battery: int
    activity: str
    source: str
    recorded_at: datetime