import unittest
from unittest.mock import MagicMock
from pawn import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.board = MagicMock()
        self.white_pawn = Pawn("WHITE", self.board)
        self.black_pawn = Pawn("BLACK", self.board)

    def test_white_pawn_single_step_forward(self):
        self.board.get_piece.return_value = None
        self.assertTrue(self.white_pawn.valid_positions(6, 0, 5, 0))

    def test_black_pawn_single_step_forward(self):
        self.board.get_piece.return_value = None
        self.assertTrue(self.black_pawn.valid_positions(1, 0, 2, 0))

    def test_white_pawn_double_step_forward(self):
        self.board.get_piece.side_effect = [None, None]
        self.assertTrue(self.white_pawn.valid_positions(6, 0, 4, 0))

    def test_black_pawn_double_step_forward(self):
        self.board.get_piece.side_effect = [None, None]
        self.assertTrue(self.black_pawn.valid_positions(1, 0, 3, 0))

    def test_white_pawn_invalid_double_step_forward(self):
        self.board.get_piece.side_effect = [None, MagicMock()]
        self.assertFalse(self.white_pawn.valid_positions(6, 0, 4, 0))

    def test_black_pawn_invalid_double_step_forward(self):
        self.board.get_piece.side_effect = [None, MagicMock()]
        self.assertFalse(self.black_pawn.valid_positions(1, 0, 3, 0))

    def test_white_pawn_capture(self):
        target_piece = MagicMock()
        target_piece.get_color.return_value = "BLACK"
        self.board.get_piece.return_value = target_piece
        self.assertTrue(self.white_pawn.valid_positions(6, 0, 5, 1))

    def test_black_pawn_capture(self):
        target_piece = MagicMock()
        target_piece.get_color.return_value = "WHITE"
        self.board.get_piece.return_value = target_piece
        self.assertTrue(self.black_pawn.valid_positions(1, 0, 2, 1))

    def test_white_pawn_invalid_capture(self):
        target_piece = MagicMock()
        target_piece.get_color.return_value = "WHITE"
        self.board.get_piece.return_value = target_piece
        self.assertFalse(self.white_pawn.valid_positions(6, 0, 5, 1))

    def test_black_pawn_invalid_capture(self):
        target_piece = MagicMock()
        target_piece.get_color.return_value = "BLACK"
        self.board.get_piece.return_value = target_piece
        self.assertFalse(self.black_pawn.valid_positions(1, 0, 2, 1))

    def test_white_pawn_invalid_move(self):
        self.board.get_piece.return_value = None
        self.assertFalse(self.white_pawn.valid_positions(6, 0, 4, 1))

    def test_black_pawn_invalid_move(self):
        self.board.get_piece.return_value = None
        self.assertFalse(self.black_pawn.valid_positions(1, 0, 3, 1))

if __name__ == '__main__':
    unittest.main()