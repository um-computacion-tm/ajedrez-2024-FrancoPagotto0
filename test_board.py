import unittest
from board import Board
from rook import Rook
from horse import Horse
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from exceptions import OutOfBoard, InvalidMove, EmptyPosition, CaptureOwnPieceError

class CaptureOwnPieceError(Exception):
    pass

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)

    def test_initialization(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertIsInstance(board.get_piece(0, 1), Horse)
        self.assertIsInstance(board.get_piece(0, 2), Bishop)
        self.assertIsInstance(board.get_piece(0, 3), Queen)
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertIsInstance(board.get_piece(1, 0), Pawn)
        self.assertIsInstance(board.get_piece(6, 0), Pawn)
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertIsInstance(board.get_piece(7, 1), Horse)
        self.assertIsInstance(board.get_piece(7, 2), Bishop)
        self.assertIsInstance(board.get_piece(7, 3), Queen)
        self.assertIsInstance(board.get_piece(7, 4), King)

    def test_get_piece(self):
        self.board.set_piece(0, 0, Rook("BLACK", self.board))
        piece = self.board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.get_color(), "BLACK")

    def test_set_piece(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(0, 0, rook)
        self.assertEqual(self.board.get_piece(0, 0), rook)

    def test_move_piece(self):
        self.board.set_piece(0, 0, Rook("BLACK", self.board))
        self.board.move(0, 0, 0, 1)
        self.assertIsInstance(self.board.get_piece(0, 1), Rook)
        self.assertIsNone(self.board.get_piece(0, 0))

    def test_move_empty_position(self):
        with self.assertRaises(EmptyPosition):
            self.board.move(0, 0, 0, 1)

    def test_invalid_move(self):
        self.board.set_piece(0, 0, Rook("BLACK", self.board))
        with self.assertRaises(InvalidMove):
            self.board.move(0, 0, 1, 2)

    def test_out_of_board(self):
        with self.assertRaises(OutOfBoard):
            self.board.get_piece(8, 8)
        with self.assertRaises(OutOfBoard):
            self.board.set_piece(8, 8, Rook("BLACK", self.board))

if __name__ == '__main__':
    unittest.main()