# AstroAlert - Space Debris Monitoring System

AstroAlert is a real-time space debris monitoring system that helps track and assess collision risks for satellites and space debris.

## Features

- Real-time 3D visualization of satellites and space debris
- Live orbit tracking and position updates
- Collision risk assessment
- Maneuver optimization suggestions
- WebSocket-based real-time updates

## Tech Stack

- **Frontend:**
  - React with TypeScript
  - Cesium.js for 3D visualization
  - TailwindCSS for styling
  - WebSocket for real-time updates

- **Backend:**
  - FastAPI (Python)
  - PostgreSQL database
  - SQLAlchemy ORM
  - SGP4 for orbital calculations

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- PostgreSQL 17.x
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/astroalert.git
   cd astroalert
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Create a PostgreSQL database named 'astroalert'
   - Update .env file with your database credentials

4. Run database migrations:
   ```bash
   alembic upgrade head
   ```

5. Set up the frontend:
   ```bash
   cd ../frontend
   npm install
   ```

## Running the Application

1. Start the backend:
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend
   npm start
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Uses TLE data format for orbital parameters
- Built with FastAPI and React
- Visualization powered by Cesium.js
