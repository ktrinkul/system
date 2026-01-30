# Project Structure Documentation

## Project Overview
This project is designed to handle video analytics through three primary components:

### 1. video_analytics_api
- `requirements.txt`: Lists the dependencies required for the API.
- `run.sh`: Shell script to run the API.
- `app/`: Contains the main application code, including:
  - `models.py`: Defines the data models.
  - `database.py`: Handles database connections and operations.
  - `__init__.py`: Initializes the application package.
  - `schemas.py`: Contains Pydantic schemas for data validation.
  - `main.py`: The main entry point for the API.
  - `routers/`: Contains route definitions, including:
    - `scenario.py`: Manages scenario-related API routes.
    - `outbox.py`: Manages outbox transactions for the API.

### 2. video_analytics_orchestrator
- `requirements.txt`: Lists the dependencies required for the orchestrator.
- `run.sh`: Shell script to run the orchestrator.
- `app/`: Contains the main application code, including:
  - `models.py`: Defines the data models for the orchestrator.
  - `database.py`: Handles database connections and operations.
  - `__init__.py`: Initializes the application package.
  - `state_machine.py`: Manages state transitions.
  - `schemas.py`: Contains Pydantic schemas for data validation.
  - `publisher.py`: Responsible for publishing results.
  - `main.py`: The main entry point for the orchestrator.
  - `routers/`: Contains route definitions, including:
    - `orchestrator.py`: Manages orchestrator-related API routes.

### 3. video_analytics_runner
- `app/`: Contains the runner application code, including:
  - `runner.py`: The main entry point for the runner.
  - `models.py`: Defines the data models used by the runner.
  - `database.py`: Handles database operations.
  - `init_db.py`: Initializes the database with initial data.
  - `19.mp4`, `29.mp4`: Sample video files for testing.

### Additional Information
- This project employs a microservices architecture, and each component can be operated independently. Ensure you have the appropriate environment set up before running each component.