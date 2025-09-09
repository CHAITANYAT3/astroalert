import numpy as np
from scipy.spatial.distance import cdist

class RiskAssessor:
    def __init__(self):
        # In a real implementation, this would load a trained model
        pass

    def calculate_risk(self, satellite_position, all_positions, time_to_closest_approach):
        """
        Calculate risk score based on position and velocity
        """
        # Simple risk calculation based on distance
        distances = cdist([satellite_position], all_positions)
        min_distance = np.min(distances[distances > 0])
        
        # Basic risk score calculation
        # Risk increases as distance decreases and time to closest approach decreases
        base_risk = 1.0 / (1.0 + min_distance)
        time_factor = 1.0 / (1.0 + time_to_closest_approach)
        
        risk_score = base_risk * time_factor
        return np.clip(risk_score, 0, 1)

    def get_nearest_objects(self, satellite_position, all_positions, n=5):
        """
        Get the n nearest objects to a satellite
        """
        distances = cdist([satellite_position], all_positions)
        nearest_indices = np.argsort(distances[0])[1:n+1]  # Exclude self
        return nearest_indices, distances[0][nearest_indices]
