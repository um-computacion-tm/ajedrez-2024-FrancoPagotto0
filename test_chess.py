import unittest
from unittest.mock import MagicMock
from board import Board
from chess import Chess

class TestChess(unittest.TestCase):

    def test_is_playing(self):
        chess_game = Chess()
        self.assertTrue(chess_game.is_playing())

    def test_change_turn(self):
        chess_game = Chess()
        self.assertEqual(chess_game.turn, "WHITE")
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "BLACK")
        chess_game.change_turn()
        self.assertEqual(chess_game.turn, "WHITE")

    def test_move_get_piece_and_change_turn(self):
        chess_game = Chess()
        mock_board = MagicMock(spec=Board)
        chess_game._Chess__board__ = mock_board
        chess_game.move(0, 1, 0, 2)
        print("Calls to get_piece:", mock_board.get_piece.call_args_list)
        self.assertEqual(chess_game.turn, "BLACK")

if __name__ == '__main__':
    unittest.main()

