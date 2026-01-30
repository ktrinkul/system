import unittest
from app.state_machine import StateMachine

class TestStateMachine(unittest.TestCase):

    def test_state_transition(self):
        sm = StateMachine()
        sm.transition('next_state')
        self.assertEqual(sm.current_state, 'next_state')

if __name__ == '__main__':
    unittest.main()