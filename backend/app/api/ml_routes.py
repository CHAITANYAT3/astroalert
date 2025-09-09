from fastapi import APIRouter, HTTPException
from app.ml.risk_assessment import assess_risk
from app.ml.maneuver_optimization import optimize_maneuver
from app.models.schemas import RiskAssessment, SpaceObject, ManeuverSuggestion
from typing import List
import numpy as np

router = APIRouter()

@router.get("/satellites/{satellite_id}/risk", response_model=RiskAssessment)
async def get_risk_assessment(satellite_id: str, current_objects: List[SpaceObject]):
    try:
        # Get the target satellite
        target = next((obj for obj in current_objects if obj.id == satellite_id), None)
        if not target:
            raise HTTPException(status_code=404, detail="Satellite not found")
            
        # Convert positions to numpy arrays for ML processing
        target_pos = np.array([target.position.x, target.position.y, target.position.z])
        target_vel = np.array([target.velocity.x, target.velocity.y, target.velocity.z])
        
        other_objects = [obj for obj in current_objects if obj.id != satellite_id]
        other_positions = np.array([[obj.position.x, obj.position.y, obj.position.z] 
                                  for obj in other_objects])
        
        # Get risk assessment
        risk_score, collision_prob, nearest_indices = assess_risk(
            target_pos, target_vel, other_positions
        )
        
        # Get nearest objects
        nearest_objects = [other_objects[i] for i in nearest_indices[:5]]
        
        # If risk is high, calculate maneuver suggestion
        maneuver_suggestion = None
        if risk_score > 0.5:
            maneuver = optimize_maneuver(
                target_pos, target_vel,
                other_positions,
                fuel_available=100.0  # Example value
            )
            if maneuver:
                maneuver_suggestion = ManeuverSuggestion(
                    deltaV=maneuver['delta_v'],
                    fuelRequired=maneuver['fuel_required'],
                    expectedMinDistance=maneuver['expected_min_distance']
                )
        
        return RiskAssessment(
            riskScore=float(risk_score),
            collisionProbability=float(collision_prob),
            nearestObjects=nearest_objects,
            suggestedManeuver=maneuver_suggestion
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
