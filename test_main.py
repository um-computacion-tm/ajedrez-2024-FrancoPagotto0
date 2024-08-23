import unittest
from unittest.mock import patch
from chess import Chess
from main import play

class TestMainS(unittest.TestCase):
    
    def run_test_scenario(self, input_values, expected_input_calls, expected_print_calls, expected_move_calls):
        with patch('builtins.input', side_effect=input_values) as mock_input, \
             patch('builtins.print') as mock_print, \
             patch.object(Chess, 'move') as mock_chess_move:
            
            chess = Chess()
            play(chess)
            
            self.assertEqual(mock_input.call_count, expected_input_calls)
            self.assertEqual(mock_print.call_count, expected_print_calls)
            self.assertEqual(mock_chess_move.call_count, expected_move_calls)

    def test_happy_path(self):
        self.run_test_scenario(
            input_values=['1', '1', '2', '2'],
            expected_input_calls=4,
            expected_print_calls=2,
            expected_move_calls=1
        )

    def test_not_happy_path(self):
        self.run_test_scenario(
            input_values=['hola', '1', '2', '2'],
            expected_input_calls=1,
            expected_print_calls=3,
            expected_move_calls=0
        )

    def test_more_not_happy_path(self):
        self.run_test_scenario(
            input_values=['1', '1', '2', 'hola'],
            expected_input_calls=4,
            expected_print_calls=3,
            expected_move_calls=0
        )

if __name__ == '__main__':
    unittest.main()
