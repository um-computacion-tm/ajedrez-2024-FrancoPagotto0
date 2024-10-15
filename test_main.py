import unittest
from unittest.mock import patch, MagicMock
from main import get_input, play
from exceptions import InvalidMove, InvalidTurn, EmptyPosition, GameOver

class TestChessGame(unittest.TestCase):

                @patch('builtins.input', side_effect=['5', 'EXIT'])
                def test_get_input_exit(self, _):
                    with self.assertRaises(GameOver):
                        get_input("Prompt")

                @patch('builtins.input', side_effect=['not_a_number', '5'])
                def test_get_input_invalid_then_valid(self, _):
                    result = get_input("Prompt")
                    self.assertEqual(result, 5)

                @patch('main.get_input', side_effect=[1, 1, 2, 2])
                def test_play_valid_move(self, _):
                    mock_chess = MagicMock()
                    play(mock_chess)
                    mock_chess.move.assert_called_with(1, 1, 2, 2)

                @patch('main.get_input', side_effect=[1, 1, 2, 2])
                def test_play_invalid_move(self, _):
                    mock_chess = MagicMock()
                    mock_chess.move.side_effect = InvalidMove("Invalid move")
                    with patch('builtins.print') as mock_print:
                        play(mock_chess)
                        mock_print.assert_any_call("Movimiento inválido: Invalid move")

                @patch('main.get_input', side_effect=[1, 1, 2, 2])
                def test_play_invalid_turn(self, _):
                    mock_chess = MagicMock()
                    mock_chess.move.side_effect = InvalidTurn("Invalid turn")
                    with patch('builtins.print') as mock_print:
                        play(mock_chess)
                        mock_print.assert_any_call("Turno inválido: Invalid turn")

                @patch('main.get_input', side_effect=[1, 1, 2, 2])
                def test_play_empty_position(self, _):
                    mock_chess = MagicMock()
                    mock_chess.move.side_effect = EmptyPosition("Empty position")
                    with patch('builtins.print') as mock_print:
                        play(mock_chess)
                        mock_print.assert_any_call("Posición vacía: Empty position")

                @patch('main.get_input', side_effect=[1, 1, 2, 2])
                def test_play_game_over(self, _):
                    mock_chess = MagicMock()
                    mock_chess.move.side_effect = GameOver("Game over")
                    with patch('builtins.print') as mock_print:
                        play(mock_chess)
                        mock_print.assert_any_call("Juego terminado: Game over")


if __name__ == '__main__':
    unittest.main()
