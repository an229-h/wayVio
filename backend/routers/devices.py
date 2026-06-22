from fastapi import APIRouter, HTTPException, Depends
from schemas.device import DeviceCreate, DeviceRegisterResponse
import uuid
import secrets

router = APIRouter(prefix="/api/v1/devices", tags=["devices"])

@router.post("/register", response_model=DeviceRegisterResponse)
async def register_device(device: DeviceCreate):
    # TODO: Add database logic to hash the token and save the device
    
    # Generate a secure random token for the device
    raw_token = secrets.token_urlsafe(32)
    
    return {
        "id": uuid.uuid4(),
        "device_name": device.device_name,
        "device_token": raw_token
    }