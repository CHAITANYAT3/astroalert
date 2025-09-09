import os
from typing import List, Dict

def load_tles(file_path: str = None) -> List[Dict]:
    """
    Load TLE data from file or use sample data if file doesn't exist
    """
    if file_path and os.path.exists(file_path):
        return load_from_file(file_path)
    else:
        return get_sample_tles()

def load_from_file(file_path: str) -> List[Dict]:
    """
    Load TLE data from a file
    """
    tles = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    # Process three lines at a time (name + TLE)
    for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            name = lines[i].strip()
            line1 = lines[i + 1].strip()
            line2 = lines[i + 2].strip()
            
            tles.append({
                'name': name,
                'line1': line1,
                'line2': line2,
                'type': 'SATELLITE' if 'ISS' in name else 'DEBRIS'
            })
    
    return tles

def get_sample_tles() -> List[Dict]:
    """
    Return sample TLE data for testing
    """
    return [
        {
            'name': 'ISS (ZARYA)',
            'line1': '1 25544U 98067A   23252.51782528  .00016717  00000-0  10270-3 0  9000',
            'line2': '2 25544  51.6416  21.2345 0004257  45.2345 314.7654 15.48987654321012',
            'type': 'SATELLITE'
        },
        {
            'name': 'DEBRIS-1',
            'line1': '1 99999U 23001A   23252.51782528  .00016717  00000-0  10270-3 0  9000',
            'line2': '2 99999  51.6416  21.2345 0004257  45.2345 314.7654 15.48987654321012',
            'type': 'DEBRIS'
        }
    ]
