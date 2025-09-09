import { useState, useEffect } from 'react';
import { OrbitUpdate } from '../types';

const useOrbitStream = () => {
  const [orbitData, setOrbitData] = useState<OrbitUpdate | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/orbits');
    
    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setOrbitData(data);
      } catch (err) {
        setError('Failed to parse orbit data');
      }
    };

    ws.onerror = (event) => {
      setError('WebSocket connection error');
    };

    ws.onclose = () => {
      setError('WebSocket connection closed');
    };

    return () => {
      ws.close();
    };
  }, []);

  return { orbitData, error };
};

export default useOrbitStream;
