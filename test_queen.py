import unittest
from queen import Queen
from piece import Piece
from board import Board

class TestQueen(unittest.TestCase):
  def setUp(self):
        self.board = Board()
        self.queen = Queen("WHITE", self.board)

  def test_valid_positions_vertical(self):
        self.assertFalse(self.queen.valid_positions(0, 0, 7, 0))
        self.assertFalse(self.queen.valid_positions(7, 0, 0, 0))

  def test_valid_positions_horizontal(self):
        self.assertFalse(self.queen.valid_positions(0, 0, 0, 7))
        self.assertFalse(self.queen.valid_positions(0, 7, 0, 0))

  def test_valid_positions_diagonal(self):
        self.assertFalse(self.queen.valid_positions(0, 0, 7, 7))
        self.assertFalse(self.queen.valid_positions(7, 7, 0, 0))
        self.assertFalse(self.queen.valid_positions(0, 7, 7, 0))
        self.assertFalse(self.queen.valid_positions(7, 0, 0, 7))

  def test_invalid_positions(self):
        self.assertFalse(self.queen.valid_positions(0, 0, 1, 2))
        self.assertFalse(self.queen.valid_positions(0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()