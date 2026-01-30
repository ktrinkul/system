from transitions import Machine

class ScenarioStateMachine:
    def __init__(self):
        self.states = ['init_startup', 'in_startup_processing', 'active', 'init_shutdown', 'in_shutdown_processing', 'inactive']
        self.transitions = [
            {'trigger': 'start', 'source': 'init_startup', 'dest': 'in_startup_processing'},
            {'trigger': 'activate', 'source': 'in_startup_processing', 'dest': 'active'},
            {'trigger': 'shutdown', 'source': 'active', 'dest': 'in_shutdown_processing'},
            {'trigger': 'stop', 'source': 'in_shutdown_processing', 'dest': 'inactive'},
        ]
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='init_startup')

    def on_enter_in_startup_processing(self):
        print('Entering in_startup_processing state...')

    def on_enter_active(self):
        print('Entering active state...')

    def on_enter_in_shutdown_processing(self):
        print('Entering in_shutdown_processing state...')

    def on_enter_inactive(self):
        print('Entering inactive state...')
