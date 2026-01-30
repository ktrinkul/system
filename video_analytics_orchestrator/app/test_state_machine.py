import unittest
from .state_machine import StateMachine

class TestStateMachine(unittest.TestCase):
    def test_state_transition(self):
        sm = StateMachine()
        sm.transition('new_state')
        self.assertEqual(sm.current_state, 'new_state')

    # Additional tests here

if __name__ == '__main__':
    unittest.main()