import React from 'react';
import { Viewer, Entity, Globe, Clock } from 'resium';
import { Cartesian3, Color, JulianDate, TimeIntervalCollection } from 'cesium';
import { SpaceObject } from '../types';

interface CesiumGlobeProps {
  objects: SpaceObject[];
  onObjectSelect: (object: SpaceObject) => void;
}

const CesiumGlobe: React.FC<CesiumGlobeProps> = ({ objects, onObjectSelect }) => {
  return (
    <Viewer full>
      <Globe enableLighting />
      {objects.map((obj) => (
        <Entity
          key={obj.id}
          name={obj.name}
          position={Cartesian3.fromArray([
            obj.position.x,
            obj.position.y,
            obj.position.z
          ])}
          point={{
            pixelSize: obj.type === 'SATELLITE' ? 10 : 5,
            color: obj.riskScore && obj.riskScore > 0.7
              ? Color.RED
              : obj.type === 'SATELLITE'
                ? Color.BLUE
                : Color.GRAY
          }}
          description={`
            Type: ${obj.type}
            Risk Score: ${obj.riskScore || 'N/A'}
            Velocity: ${Math.sqrt(
              obj.velocity.x ** 2 +
              obj.velocity.y ** 2 +
              obj.velocity.z ** 2
            ).toFixed(2)} km/s
          `}
          onClick={() => onObjectSelect(obj)}
        />
      ))}
    </Viewer>
  );
};

export default CesiumGlobe;
