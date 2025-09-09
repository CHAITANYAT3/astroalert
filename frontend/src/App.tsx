import React, { useState, useEffect } from 'react';
import CesiumGlobe from './components/CesiumGlobe';
import SidePanel from './components/SidePanel';
import useOrbitStream from './hooks/useOrbitStream';
import { SpaceObject, RiskAssessment } from './types';

const App: React.FC = () => {
  const { orbitData, error } = useOrbitStream();
  const [selectedObject, setSelectedObject] = useState<SpaceObject | null>(null);
  const [riskAssessment, setRiskAssessment] = useState<RiskAssessment | null>(null);

  useEffect(() => {
    if (selectedObject) {
      // Fetch risk assessment from backend
  fetch(`${process.env.REACT_APP_API_URL}/api/satellites/${selectedObject.id}/risk`)
        .then(res => res.json())
        .then(data => setRiskAssessment(data))
        .catch(err => console.error('Failed to fetch risk assessment:', err));
    }
  }, [selectedObject]);

  if (error) {
    return (
      <div className="h-screen flex items-center justify-center bg-red-50">
        <div className="text-red-600 text-xl p-4 rounded-lg bg-white shadow-lg">
          <h2 className="font-bold mb-2">Connection Error</h2>
          <p>{error}</p>
          <button 
            onClick={() => window.location.reload()} 
            className="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Retry Connection
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen w-screen relative">
      <CesiumGlobe
        objects={orbitData?.objects || []}
        onObjectSelect={setSelectedObject}
      />
      <SidePanel
        selectedObject={selectedObject}
        riskAssessment={riskAssessment}
      />
    </div>
  );
};

export default App;
