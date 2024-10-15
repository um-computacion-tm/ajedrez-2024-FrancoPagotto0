from chess import Chess
import unittest
from unittest.mock import MagicMock
from exceptions import EmptyPosition, InvalidTurn, InvalidMove

class TestChess(unittest.TestCase):
        def setUp(self):
            self.chess = Chess()
            self.mock_board = MagicMock()
            self.chess._Chess__board__ = self.mock_board

        def test_move_valid(self):
            # Configura el tablero y el turno para que el movimiento sea válido
            self.chess._Chess__turn__ = "WHITE"
            mock_piece = MagicMock()
            mock_piece.get_color.return_value = "WHITE"
            mock_piece.valid_positions.return_value = True
            self.mock_board.get_piece.return_value = mock_piece

            self.chess.move(0, 0, 1, 1)
            self.assertEqual(self.chess.get_turn(), "BLACK")
            self.mock_board.move.assert_called_once_with(0, 0, 1, 1)

        def test_move_empty_position(self):
            self.mock_board.get_piece.return_value = None
            with self.assertRaises(EmptyPosition):
                self.chess.move(0, 0, 1, 1)

        def test_move_invalid_turn(self):
            self.chess._Chess__turn__ = "WHITE"
            piece = MagicMock()
            piece.get_color.return_value = "BLACK"
            self.mock_board.get_piece.return_value = piece

            with self.assertRaises(InvalidMove):
                self.chess.move(0, 0, 1, 1)

        def test_move_invalid_move(self):
            self.chess._Chess__turn__ = "WHITE"
            piece = MagicMock()
            piece.get_color.return_value = "WHITE"
            piece.valid_positions.return_value = False
            self.mock_board.get_piece.return_value = piece

            with self.assertRaises(InvalidMove):
                self.chess.move(0, 0, 1, 1)

    

if __name__ == '__main__':
    unittest.main()