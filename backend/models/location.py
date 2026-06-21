from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.base import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    device_id = Column(UUID(as_uuid=True), ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)
    client_point_id = Column(UUID(as_uuid=True), nullable=False)
    
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    accuracy_meters = Column(Float, nullable=False)
    battery_percent = Column(Integer, nullable=False)
    activity_type = Column(String, default="unknown", nullable=False)
    source = Column(String, default="gps", nullable=False)
    
    recorded_at = Column(DateTime(timezone=True), nullable=False)
    received_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    upload_session_id = Column(UUID(as_uuid=True), nullable=False)

    __table_args__ = (
        UniqueConstraint("device_id", "client_point_id", name="unique_device_client_point"),
        Index("idx_locations_device_recorded_at", "device_id", "recorded_at"),
    )