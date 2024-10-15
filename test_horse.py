import unittest
from horse import Horse

class MockBoard:
            def __init__(self):
                self.board = [[None for _ in range(8)] for _ in range(8)]

            def get_piece(self, row, col):
                return self.board[row][col]

            def set_piece(self, row, col, piece):
                self.board[row][col] = piece

class TestHorse(unittest.TestCase):
            def setUp(self):
                self.mock_board = MockBoard()
                self.horse = Horse("WHITE", self.mock_board)
                self.mock_board.set_piece(4, 4, self.horse)
                self.horse.set_position(4, 4)

            def test_valid_positions_true(self):
                # Test valid L-shaped moves
                self.assertTrue(self.horse.valid_positions(4, 4, 6, 5))
                self.assertTrue(self.horse.valid_positions(4, 4, 6, 3))
                self.assertTrue(self.horse.valid_positions(4, 4, 2, 5))
                self.assertTrue(self.horse.valid_positions(4, 4, 2, 3))
                self.assertTrue(self.horse.valid_positions(4, 4, 5, 6))
                self.assertTrue(self.horse.valid_positions(4, 4, 5, 2))
                self.assertTrue(self.horse.valid_positions(4, 4, 3, 6))
                self.assertTrue(self.horse.valid_positions(4, 4, 3, 2))

            def test_valid_positions_false(self):
                # Test invalid moves
                self.assertFalse(self.horse.valid_positions(4, 4, 4, 4))  # Same position
                self.assertFalse(self.horse.valid_positions(4, 4, 5, 5))  # Diagonal move
                self.assertFalse(self.horse.valid_positions(4, 4, 4, 5))  # Horizontal move
                self.assertFalse(self.horse.valid_positions(4, 4, 5, 4))  # Vertical move

            def test_valid_positions_with_obstacles(self):
                # Place a piece of the same color in the path
                blocking_piece = Horse("WHITE", self.mock_board)
                self.mock_board.set_piece(6, 5, blocking_piece)
                self.assertFalse(self.horse.valid_positions(4, 4, 6, 5))

                # Place a piece of the opposite color in the path
                enemy_piece = Horse("BLACK", self.mock_board)
                self.mock_board.set_piece(6, 5, enemy_piece)
                self.assertTrue(self.horse.valid_positions(4, 4, 6, 5))

 
            
if __name__ == '__main__':
    unittest.main()