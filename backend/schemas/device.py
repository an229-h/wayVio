from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class DeviceCreate(BaseModel):
    device_name: str

class DeviceRegisterResponse(BaseModel):
    id: UUID
    device_name: str
    device_token: str

class DeviceResponse(BaseModel):
    id: UUID
    device_name: str
    tracking_enabled: bool
    last_seen: datetime

    class Config:
        from_attributes = True