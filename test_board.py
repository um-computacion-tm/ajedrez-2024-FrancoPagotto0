import unittest
from board import Board
from rook import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        def test_get_piece_initial_positions(self):
        # posicione iniciales del tablero
          self.assertIsInstance(self.board.get_piece(0, 0), Rook)
          self.assertIsInstance(self.board.get_piece(0, 7), Rook)
          self.assertIsInstance(self.board.get_piece(7, 0), Rook)
          self.assertIsInstance(self.board.get_piece(7, 7), Rook)

        #  color de las piezas en pos inicial
          self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
          self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
          self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
          self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

    def test_get_piece_empty_positions(self):
        # Verifica que las posiciones vacías den none
          self.assertIsNone(self.board.get_piece(3, 1))
          self.assertIsNone(self.board.get_piece(4, 4))
          self.assertIsNone(self.board.get_piece(5, 2))
    

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (   
                "♖♘    ♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞    ♞♜\n"
            )
        )
if __name__ == '__main__':
    unittest.main()
