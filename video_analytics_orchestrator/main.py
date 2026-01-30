def main():
    """Entry point for the orchestrator service. Manages the state of video analytics jobs."""
    try:
        # Initialize state machine and orchestrator settings
        state_machine = create_state_machine()
        # Monitor and respond to API requests
        run_orchestrator(state_machine)
    except Exception as e:
        # Log the error for diagnostics
        print(f'Error within orchestrator: {e}')
        raise
