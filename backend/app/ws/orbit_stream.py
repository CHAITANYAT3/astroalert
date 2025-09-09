import asyncio
from fastapi import WebSocket
from datetime import datetime
from sgp4.api import Satrec, jday
from typing import List, Dict
from app.utils.tle_loader import load_tles
from app.models.schemas import OrbitPosition

async def orbit_streamer(websocket: WebSocket):
    """
    Streams real-time orbital positions to connected clients
    """
    await websocket.accept()
    try:
        # Load initial TLE data
        tles = load_tles()
        
        while True:
            # Get current time
            now = datetime.utcnow()
            jd, fr = jday(now.year, now.month, now.day,
                         now.hour, now.minute, now.second)
            
            # Calculate positions for all objects
            positions = []
            for tle in tles:
                sat = Satrec.twoline2rv(tle['line1'], tle['line2'])
                error, position, velocity = sat.sgp4(jd, fr)
                
                if not error:
                    positions.append({
                        "id": tle.get('id', ''),
                        "name": tle.get('name', ''),
                        "position": {
                            "x": position[0],
                            "y": position[1],
                            "z": position[2]
                        },
                        "velocity": {
                            "x": velocity[0],
                            "y": velocity[1],
                            "z": velocity[2]
                        },
                        "type": tle.get('type', 'UNKNOWN')
                    })
            
            # Send position updates to client
            await websocket.send_json({
                "timestamp": now.isoformat(),
                "objects": positions
            })
            
            # Wait before next update
            await asyncio.sleep(1)
            
    except Exception as e:
        print(f"Error in orbit streamer: {str(e)}")
    finally:
        await websocket.close()
