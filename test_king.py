import unittest
from unittest.mock import MagicMock
from king import King
from board import Board

class TestKing(unittest.TestCase):
    def setUp(self):
        self.mock_board = MagicMock(spec=Board)
        self.king = King("WHITE", self.mock_board)
        self.king.set_position(4, 4)  # Set initial position for the king

    def test_valid_positions_vertical_horizontal(self):
        self.assertTrue(self.king.valid_positions(4, 4, 5, 4))  # Move down
        self.assertTrue(self.king.valid_positions(4, 4, 4, 5))  # Move right
        self.assertTrue(self.king.valid_positions(4, 4, 4, 3))  # Move left
        self.assertTrue(self.king.valid_positions(4, 4, 3, 4))  # Move up

    def test_valid_positions_diagonal(self):
        self.assertTrue(self.king.valid_positions(4, 4, 5, 5))  # Move down-right
        self.assertTrue(self.king.valid_positions(4, 4, 5, 3))  # Move down-left
        self.assertTrue(self.king.valid_positions(4, 4, 3, 5))  # Move up-right
        self.assertTrue(self.king.valid_positions(4, 4, 3, 3))  # Move up-left

    def test_invalid_positions(self):
        self.assertFalse(self.king.valid_positions(4, 4, 6, 4))  # Move two steps down
        self.assertFalse(self.king.valid_positions(4, 4, 4, 6))  # Move two steps right
        self.assertFalse(self.king.valid_positions(4, 4, 2, 2))  # Move two steps diagonally

if __name__ == '__main__':
    unittest.main()