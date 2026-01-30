import requests

class Runner:
    def __init__(self):
        self.state = "inactive"
    
    def update_state(self, new_state: str):
        """Update runner state based on orchestrator state changes."""
        self.state = new_state
        # Notify the orchestrator of the new state if needed
    
    def run(self):
        """Main logic to run video processing."""
        if self.state == "active":
            pass  # Main run logic when active
