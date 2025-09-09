export interface Position {
  x: number;
  y: number;
  z: number;
}

export interface Velocity {
  x: number;
  y: number;
  z: number;
}

export interface SpaceObject {
  id: string;
  name: string;
  position: Position;
  velocity: Velocity;
  type: 'SATELLITE' | 'DEBRIS';
  riskScore?: number;
}

export interface RiskAssessment {
  riskScore: number;
  collisionProbability: number;
  nearestObjects: SpaceObject[];
  suggestedManeuver?: {
    deltaV: Velocity;
    fuelRequired: number;
    expectedMinDistance: number;
  };
}

export interface OrbitUpdate {
  timestamp: string;
  objects: SpaceObject[];
}
