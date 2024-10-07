import unittest
from unittest.mock import MagicMock, patch
from chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition




class TestChess(unittest.TestCase):

    @patch('board.Board')
    def setUp(self, MockBoard):
        self.mock_board = MockBoard.return_value
        self.chess = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess._Chess__turn__, "WHITE")

    def test_get_board(self):
        self.assertEqual(self.chess.get_board(), self.mock_board)

    def test_move_empty_position(self):
        self.mock_board.get_piece.return_value = None
        with self.assertRaises(EmptyPosition):
            self.chess.move(0, 0, 1, 1)

    def test_move_invalid_turn(self):
        mock_piece = MagicMock()
        mock_piece.get_color.return_value = "BLACK"
        self.mock_board.get_piece.return_value = mock_piece
        with self.assertRaises(InvalidTurn):
            self.chess.move(0, 0, 1, 1)

    def test_move_invalid_move(self):
        mock_piece = MagicMock()
        mock_piece.get_color.return_value = "WHITE"
        mock_piece.valid_positions.return_value = False
        self.mock_board.get_piece.return_value = mock_piece
        with self.assertRaises(InvalidMove):
            self.chess.move(0, 0, 1, 1)

    def test_move_valid(self):
        mock_piece = MagicMock()
        mock_piece.get_color.return_value = "WHITE"
        mock_piece.valid_positions.return_value = True
        self.mock_board.get_piece.return_value = mock_piece

        self.chess.move(0, 0, 1, 1)
        self.mock_board.move.assert_called_once_with(0, 0, 1, 1)
        self.assertEqual(self.chess._Chess__turn__, "BLACK")

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess._Chess__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess._Chess__turn__, "WHITE")

if __name__ == '__main__':
    unittest.main()
