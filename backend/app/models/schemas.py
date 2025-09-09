from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class Position(BaseModel):
    x: float
    y: float
    z: float

class Velocity(BaseModel):
    x: float
    y: float
    z: float

class OrbitPosition(BaseModel):
    id: str
    name: str
    position: Dict[str, float]
    velocity: Dict[str, float]
    type: str

class SatelliteData(BaseModel):
    id: str
    name: str
    norad_id: Optional[str]
    position: Position
    velocity: Velocity
    last_update: datetime
    object_type: str  # 'SATELLITE' or 'DEBRIS'
    risk_score: Optional[float]

class RiskAssessment(BaseModel):
    risk_score: float
    collision_probability: float
    nearest_objects: List[SatelliteData]
