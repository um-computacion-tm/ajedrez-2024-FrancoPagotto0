import unittest
from rook import Rook
from board import Board

class TestRook(unittest.TestCase):
    
    def setUp(self):
        self.board = Board(for_test=True)  # Crear un tablero vacío para pruebas
        self.rook = Rook("WHITE", self.board)

    def test_valid_positions(self):
        # Test valid horizontal move
        self.assertTrue(self.rook.valid_positions(0, 0, 0, 7))
        # Test valid vertical move
        self.assertTrue(self.rook.valid_positions(0, 0, 7, 0))
        # Test invalid move (diagonal)
        self.assertFalse(self.rook.valid_positions(0, 0, 7, 7))
        # Test invalid move (L-shape)
        self.assertFalse(self.rook.valid_positions(0, 0, 2, 1))

    def test_possible_moves(self):
        # Test possible moves from the center of the board
        expected_moves = [
            (4, 3), (5, 3), (6, 3), (7, 3),  # Down
            (2, 3), (1, 3), (0, 3),          # Up
            (3, 4), (3, 5), (3, 6), (3, 7),  # Right
            (3, 2), (3, 1), (3, 0)           # Left
        ]
        self.assertCountEqual(self.rook.possible_moves(3, 3, [(1, 0), (-1, 0), (0, 1), (0, -1)]), expected_moves)

        # Test possible moves from a corner of the board
        expected_moves = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Down
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Right
        ]
        self.assertCountEqual(self.rook.possible_moves(0, 0, [(1, 0), (-1, 0), (0, 1), (0, -1)]), expected_moves)

if __name__ == '__main__':
    unittest.main()