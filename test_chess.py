import unittest
from chess import Chess

class TestChess(unittest.TestCase):

    def test_change_turn_white_to_black(self):
        chess_game = Chess()
        self.assertEqual(chess_game.turn, "WHITE")
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "BLACK")

    def test_change_turn_black_to_white(self):
        chess_game = Chess()
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "BLACK")
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "WHITE")

if __name__ == '__main__':
    unittest.main()
