## Video Analytics System Overview

### API
- POST /scenario/ - Initializes state machine
- POST /scenario/<scenario_id>/ - Change status of the state machine
- GET /scenario/<scenario_id>/ - Information about the current status
- GET /prediction/<scenario_id>/ - Prediction results

### Orchestrator
- Handle events and manage state machine

### Runner
- Process video feed and handle inference and results.