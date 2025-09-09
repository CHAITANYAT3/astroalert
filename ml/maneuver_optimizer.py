import numpy as np
from scipy.optimize import minimize

class ManeuverOptimizer:
    def __init__(self):
        self.fuel_weight = 0.7  # Weight for fuel consumption in optimization
        self.safety_weight = 0.3  # Weight for safety in optimization

    def optimize_maneuver(self, current_state, hazard_states, fuel_available):
        """
        Optimize satellite maneuver considering both safety and fuel consumption
        
        Args:
            current_state: dict with position and velocity
            hazard_states: list of dicts with positions and velocities of hazards
            fuel_available: float representing available fuel
            
        Returns:
            dict with optimal delta-v maneuver
        """
        def objective(delta_v):
            # Calculate new state after maneuver
            new_velocity = [
                current_state['velocity']['x'] + delta_v[0],
                current_state['velocity']['y'] + delta_v[1],
                current_state['velocity']['z'] + delta_v[2]
            ]
            
            # Calculate fuel cost (normalized by available fuel)
            fuel_cost = np.linalg.norm(delta_v) / fuel_available
            
            # Calculate safety metric (minimum distance to hazards)
            min_distance = float('inf')
            for hazard in hazard_states:
                distance = np.linalg.norm([
                    current_state['position']['x'] - hazard['position']['x'],
                    current_state['position']['y'] - hazard['position']['y'],
                    current_state['position']['z'] - hazard['position']['z']
                ])
                min_distance = min(min_distance, distance)
            
            safety_metric = 1.0 / (1.0 + min_distance)
            
            # Combined cost function
            return (self.fuel_weight * fuel_cost + 
                   self.safety_weight * safety_metric)
        
        # Initial guess: no maneuver
        x0 = np.zeros(3)
        
        # Constraints: fuel limitation
        constraints = [{
            'type': 'ineq',
            'fun': lambda x: fuel_available - np.linalg.norm(x)
        }]
        
        # Optimize
        result = minimize(
            objective,
            x0,
            method='SLSQP',
            constraints=constraints
        )
        
        if result.success:
            return {
                'delta_v': {
                    'x': result.x[0],
                    'y': result.x[1],
                    'z': result.x[2]
                },
                'fuel_required': np.linalg.norm(result.x),
                'expected_min_distance': 1.0 / (result.fun / self.safety_weight) - 1.0
            }
        else:
            return None
