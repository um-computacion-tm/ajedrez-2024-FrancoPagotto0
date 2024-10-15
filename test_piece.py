import unittest
from unittest.mock import MagicMock
from piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.mock_board = MagicMock()
        self.piece = Piece("WHITE", self.mock_board)

    def test_get_color(self):
        self.assertEqual(self.piece.get_color(), "WHITE")

    def test_get_board(self):
        self.assertEqual(self.piece.get_board(), self.mock_board)

    def test_set_position(self):
        self.piece.set_position(3, 4)
        self.assertEqual(self.piece._Piece__row, 3)
        self.assertEqual(self.piece._Piece__col, 4)

    def test_is_within_board(self):
        self.assertTrue(self.piece.is_within_board(0, 0))
        self.assertTrue(self.piece.is_within_board(7, 7))
        self.assertFalse(self.piece.is_within_board(-1, 0))
        self.assertFalse(self.piece.is_within_board(0, 8))

    def test_possible_moves(self):
        self.mock_board.get_piece.return_value = None
        directions = [(1, 0), (0, 1)]
        moves = self.piece.possible_moves(3, 3, directions)
        expected_moves = [(4, 3), (5, 3), (6, 3), (7, 3), (3, 4), (3, 5), (3, 6), (3, 7)]
        self.assertEqual(moves, expected_moves)

    def test_possible_moves_with_obstacle(self):
        obstacle_piece = MagicMock()
        obstacle_piece.get_color.return_value = "BLACK"
        self.mock_board.get_piece.side_effect = [None, obstacle_piece, None]
        directions = [(1, 0)]
        moves = self.piece.possible_moves(3, 3, directions)
        expected_moves = [(4, 3), (5, 3)]
        self.assertEqual(moves, expected_moves)

    def test_possible_moves_single_step(self):
        self.mock_board.get_piece.return_value = None
        directions = [(1, 0)]
        moves = self.piece.possible_moves(3, 3, directions, single_step=True)
        expected_moves = [(4, 3)]
        self.assertEqual(moves, expected_moves)

    def test_valid_positions_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.piece.valid_positions()

if __name__ == '__main__':
    unittest.main()