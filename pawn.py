from piece import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        direction = -1 if self.get_color() == "WHITE" else 1  # Determina la dirección del movimiento
        

        # Movimiento hacia adelante
        if from_col == to_col:
            if to_row == from_row + direction:
                # Movimiento de una casilla hacia adelante
                if self.get_board().get_piece(to_row, to_col) is None:
                    return True
            if from_col == to_col and to_row == from_row + 2 * direction:
                # Movimiento de dos casillas desde la posición inicial
                if self.get_board().get_piece(to_row, to_col) is None and self.get_board().get_piece(from_row + direction, from_col) is None:
                    
                    return True

        # Captura en diagonal
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            target_piece = self.get_board().get_piece(to_row, to_col)
            if target_piece is not None and target_piece.get_color() != self.get_color():
                return True  # Movimiento en diagonal para captura

        return False

    def __str__(self):
        return self.white_str if self.get_color() == "WHITE" else self.black_str