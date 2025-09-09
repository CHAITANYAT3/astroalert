import numpy as np
from scipy.spatial.distance import cdist
from typing import Tuple, List

def assess_risk(target_position: np.ndarray,
               target_velocity: np.ndarray,
               other_positions: np.ndarray,
               time_horizon: float = 24.0) -> Tuple[float, float, List[int]]:
    """
    Assess collision risk for a target satellite
    
    Args:
        target_position: [x, y, z] position of target satellite
        target_velocity: [vx, vy, vz] velocity of target satellite
        other_positions: Nx3 array of other object positions
        time_horizon: Hours to look ahead for collision risk
    
    Returns:
        risk_score: Overall risk score (0-1)
        collision_probability: Probability of collision
        nearest_indices: Indices of nearest objects
    """
    # Calculate distances to all other objects
    distances = cdist([target_position], other_positions)[0]
    
    # Get indices of nearest objects
    nearest_indices = np.argsort(distances)
    
    # Calculate minimum distance
    min_distance = distances[nearest_indices[0]]
    
    # Simple collision probability based on distance
    collision_probability = 1.0 / (1.0 + np.exp(min_distance / 1000 - 5))
    
    # Calculate relative velocities
    relative_velocity = np.linalg.norm(target_velocity)
    
    # Risk score combines distance and velocity
    risk_score = collision_probability * (relative_velocity / 10000)
    risk_score = np.clip(risk_score, 0, 1)
    
    return risk_score, collision_probability, nearest_indices.tolist()
