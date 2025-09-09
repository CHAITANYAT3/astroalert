from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class SpaceObject(Base):
    __tablename__ = "space_objects"

    id = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), nullable=False)  # 'satellite' or 'debris'
    tle_line1 = Column(String(100), nullable=False)
    tle_line2 = Column(String(100), nullable=False)
    last_update = Column(DateTime, default=datetime.utcnow)

    risk_assessments = relationship("RiskAssessment", back_populates="space_object")

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(Integer, primary_key=True)
    object_id = Column(String(50), ForeignKey("space_objects.id"))
    collision_probability = Column(Float, nullable=False)
    time_to_closest_approach = Column(Float, nullable=False)
    minimum_distance = Column(Float, nullable=False)
    assessment_time = Column(DateTime, default=datetime.utcnow)

    space_object = relationship("SpaceObject", back_populates="risk_assessments")
