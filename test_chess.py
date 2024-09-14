import unittest
from unittest.mock import MagicMock
from board import Board
from chess import Chess
from exceptions import EmptyPosition 

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
        # Crear un mock del tablero
        mock_board = MagicMock(spec=Board)
        
        # Crear un mock de la pieza y configurar su color
        mock_piece = MagicMock()
        mock_piece.get_color.return_value = "WHITE"
        # Configurar el mock del tablero para devolver la pieza en la posición (0, 1)
        mock_board.get_piece.side_effect = lambda row, col: mock_piece if (row, col) == (0, 1) else None
        
        # Crear una instancia de Chess y asignar el mock del tablero
        chess_game = Chess()
        chess_game._Chess__board__ = mock_board
        
        # Llamar al método move y manejar la excepción para ver qué está fallando
        try:
            chess_game.move(0, 1, 0, 2)
        except EmptyPosition:
            print("Excepción de posición vacía")

        # Verificar que get_piece fue llamado con las posiciones correctas
        mock_board.get_piece.assert_any_call(0, 1)
        mock_board.get_piece.assert_any_call(0, 2)
        
        # Verificar que el turno cambió a "BLACK"
        self.assertEqual(chess_game.turn, "BLACK")

if __name__ == '__main__':
    unittest.main()

