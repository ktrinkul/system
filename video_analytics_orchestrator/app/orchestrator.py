from state_machine import ScenarioStateMachine

class Orchestrator:
    def __init__(self):
        self.state_machine = ScenarioStateMachine()

    def handle_event(self, event):
        if event == 'start':
            self.state_machine.start()
        elif event == 'activate':
            self.state_machine.activate()
        elif event == 'shutdown':
            self.state_machine.shutdown()
        elif event == 'stop':
            self.state_machine.stop()
        print(f'Current State: {self.state_machine.state}')
