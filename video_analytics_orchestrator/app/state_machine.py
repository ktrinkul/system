from transitions import Machine
from app.models import ScenarioStatus

class ScenarioFSM:
    states = [
        ScenarioStatus.init_startup,
        ScenarioStatus.in_startup_processing,
        ScenarioStatus.active,
        ScenarioStatus.init_shutdown,
        ScenarioStatus.in_shutdown_processing,
        ScenarioStatus.inactive
    ]

    transitions = [
        { "trigger": "do_startup", "source": ScenarioStatus.init_startup,          "dest": ScenarioStatus.in_startup_processing },
        { "trigger": "complete_startup", "source": ScenarioStatus.in_startup_processing, "dest": ScenarioStatus.active },
        { "trigger": "do_shutdown",   "source": ScenarioStatus.init_shutdown,         "dest": ScenarioStatus.in_shutdown_processing },
        { "trigger": "complete_shutdown","source": ScenarioStatus.in_shutdown_processing,"dest": ScenarioStatus.inactive },
    ]

    def __init__(self, initial: ScenarioStatus):
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial=initial)

    def next(self, target: ScenarioStatus):
        # Простая логика: в зависимости от target, вызываем нужный trigger
        if target == ScenarioStatus.in_startup_processing:
            return self.do_startup()
        if target == ScenarioStatus.active:
            return self.complete_startup()
        if target == ScenarioStatus.in_shutdown_processing:
            return self.do_shutdown()
        if target == ScenarioStatus.inactive:
            return self.complete_shutdown()
        # init_startup и init_shutdown инициируются извне
        return None
