class StateMachine:
    def __init__(self):
        # Initialization of state machine variables
        self.state = 'init_startup'
        self.transitions = {
            'init_startup': ['in_startup_processing'],
            'in_startup_processing': ['active'],
            'active': ['init_shutdown'],
            'init_shutdown': ['in_shutdown_processing'],
            'in_shutdown_processing': ['inactive']
        }

    def transition(self, new_state: str) -> None:
        if new_state in self.transitions[self.state]:
            self.state = new_state
        else:
            raise ValueError(f'Invalid transition from {self.state} to {new_state}')

    def get_state(self) -> str:
        return self.state

# Add any additional state machine logic or enhancements here.
