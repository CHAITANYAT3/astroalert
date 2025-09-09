import React from 'react';
import { SpaceObject, RiskAssessment } from '../types';

interface SidePanelProps {
  selectedObject: SpaceObject | null;
  riskAssessment: RiskAssessment | null;
}

const SidePanel: React.FC<SidePanelProps> = ({ selectedObject, riskAssessment }) => {
  if (!selectedObject) {
    return null;
  }

  return (
    <div className="fixed right-0 top-0 h-full w-96 bg-white shadow-lg p-6 overflow-y-auto">
      <h2 className="text-2xl font-bold mb-4">{selectedObject.name}</h2>
      
      <div className="mb-6">
        <h3 className="text-lg font-semibold mb-2">Object Details</h3>
        <div className="grid grid-cols-2 gap-2">
          <div>Type:</div>
          <div>{selectedObject.type}</div>
          <div>Position:</div>
          <div>
            X: {selectedObject.position.x.toFixed(2)}<br />
            Y: {selectedObject.position.y.toFixed(2)}<br />
            Z: {selectedObject.position.z.toFixed(2)}
          </div>
          <div>Velocity:</div>
          <div>
            X: {selectedObject.velocity.x.toFixed(2)}<br />
            Y: {selectedObject.velocity.y.toFixed(2)}<br />
            Z: {selectedObject.velocity.z.toFixed(2)}
          </div>
        </div>
      </div>

      {riskAssessment && (
        <>
          <div className="mb-6">
            <h3 className="text-lg font-semibold mb-2">Risk Assessment</h3>
            <div className={`text-xl font-bold mb-2 ${
              riskAssessment.riskScore > 0.7 ? 'text-red-600' :
              riskAssessment.riskScore > 0.4 ? 'text-yellow-600' :
              'text-green-600'
            }`}>
              Risk Score: {(riskAssessment.riskScore * 100).toFixed(1)}%
            </div>
            <div>
              Collision Probability: {(riskAssessment.collisionProbability * 100).toFixed(2)}%
            </div>
          </div>

          {riskAssessment.suggestedManeuver && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold mb-2">Suggested Maneuver</h3>
              <div className="grid grid-cols-2 gap-2">
                <div>Delta-V:</div>
                <div>
                  X: {riskAssessment.suggestedManeuver.deltaV.x.toFixed(2)}<br />
                  Y: {riskAssessment.suggestedManeuver.deltaV.y.toFixed(2)}<br />
                  Z: {riskAssessment.suggestedManeuver.deltaV.z.toFixed(2)}
                </div>
                <div>Fuel Required:</div>
                <div>{riskAssessment.suggestedManeuver.fuelRequired.toFixed(2)} units</div>
                <div>Expected Min Distance:</div>
                <div>{riskAssessment.suggestedManeuver.expectedMinDistance.toFixed(2)} km</div>
              </div>
            </div>
          )}

          {riskAssessment.nearestObjects.length > 0 && (
            <div>
              <h3 className="text-lg font-semibold mb-2">Nearest Objects</h3>
              <div className="space-y-2">
                {riskAssessment.nearestObjects.map((obj) => (
                  <div key={obj.id} className="p-2 bg-gray-100 rounded">
                    <div className="font-semibold">{obj.name}</div>
                    <div className="text-sm">Type: {obj.type}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default SidePanel;
