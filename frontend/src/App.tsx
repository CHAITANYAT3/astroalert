import React, { useState, useEffect } from 'react';
import CesiumGlobe from './components/CesiumGlobe';
import SidePanel from './components/SidePanel';
import { SpaceObject, RiskAssessment } from './types';

const App: React.FC = () => {
  const [orbitData, setOrbitData] = useState<{ objects: SpaceObject[] } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedObject, setSelectedObject] = useState<SpaceObject | null>(null);
  const [riskAssessment, setRiskAssessment] = useState<RiskAssessment | null>(null);

  // Polling function to fetch orbit data
 async function fetchOrbitData(retries = 3) {
  try {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/api/orbit`);
    const data = await response.json();
    setOrbitData(data);
  } catch (err) {
    if (retries > 0) {
      setTimeout(() => fetchOrbitData(retries - 1), 3000); // retry after 3s
    } else {
      setError("Failed to fetch orbit data");
    }
  }
}


  // Poll every 5 seconds
  useEffect(() => {
    fetchOrbitData(); // initial fetch
    const interval = setInterval(fetchOrbitData, 5000);
    return () => clearInterval(interval); // cleanup
  }, []);

  // Fetch risk assessment when a satellite is selected
  useEffect(() => {
    if (selectedObject) {
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
      <CesiumGlobe objects={orbitData?.objects || []} onObjectSelect={setSelectedObject} />
      <SidePanel selectedObject={selectedObject} riskAssessment={riskAssessment} />
    </div>
  );
};

export default App;
