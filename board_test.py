import unittest
from board import Board
from piece import Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
    
    def test_Inicio_Tablero(self):
        self.assertEqual(len(self.board.position), 8)
        self.assertEqual(len(self.board.position[0]), 8)
        
    def test_Inicio_de_torre(self):
         self.assertIsInstance(self.board.get_piece(0, 0), Rook)
         self.assertIsInstance(self.board.get_piece(0, 7), Rook)
         self.assertIsInstance(self.board.get_piece(7, 0), Rook)
         self.assertIsInstance(self.board.get_piece(7, 7), Rook)
    
    def test_rook_colors(self):
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

    def test_Pos_fuera_del_tablero(self):
        with self.assertRaises(IndexError):
            self.board.get_piece(8, 0)

    def test_Metodo_get_piece(self):
        rook = self.board.get_piece(0, 0)
        self.assertIsInstance(rook, Rook)
        self.assertEqual(rook.color, "BLACK")

    unittest.main()



        
