import unittest
from unittest.mock import patch
from chess import Chess
from main import play


class TestMain(unittest.TestCase):
    @patch(
        'builtins.input',
        side_effect=['1', '1', '2', '2'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch(
        'builtins.input',
        side_effect=['hola', '1', '2', '2'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)
        mock_print.assert_any_call("Ingrsar numero valido en filas y columnas.")

    @patch(
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)
        mock_print.assert_any_call("Ingrsar numero valido en filas y columnas.")

    @patch('builtins.input', side_effect=KeyboardInterrupt)
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_keyboard_interrupt(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess = Chess()
        with self.assertRaises(SystemExit):
            play(chess)
        mock_print.assert_any_call("\nJuego interrumpido por el usuario")
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move', side_effect=Exception("Test Exception"))
    def test_general_exception(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess = Chess()
        play(chess)
        #verifica que el print  sea llamado con los dos  argumentos correctos
        calls = [call for call in mock_print.call_args_list if "Ocurrio un error:" in call[0]]
        self.assertEqual(mock_chess_move.call_count, 1)
if __name__ == '__main__':
    unittest.main()