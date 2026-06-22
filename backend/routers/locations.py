from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from schemas.location import LocationCreate

router = APIRouter(prefix="/api/v1/locations", tags=["locations"])

@router.post("/batch")
async def upload_locations(locations: List[LocationCreate]):
    # TODO: Verify the device token from the headers
    # TODO: Insert with ON CONFLICT (device_id, client_point_id) DO NOTHING
    
    return {"accepted": True}

@router.get("/latest/{device_id}")
async def get_latest_location(device_id: UUID):
    # TODO: Verify the human user's JWT and permissions
    # TODO: Fetch and return the latest location
    
    return {"message": "Latest location placeholder"}