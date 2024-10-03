from piece import Piece

class Pawn(Piece):
    white_str = "♟"
    black_str = "♙"

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
    
       
        direction = 1 if self.get_color() == "WHITE" else -1  # Determina la dirección del movimiento
        start_row = 6 if self.get_color() == "WHITE" else 1  # Fila inicial para los peones

        # Movimiento hacia adelante
        if from_col == to_col and to_row == from_row + direction:
            return True  # Movimiento de una casilla hacia adelante
        if from_col == to_col and from_row == start_row and to_row == from_row + 2 * direction:
            return True  # Movimiento de dos casillas desde la posición inicial

        # Captura
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            return True  # Movimiento en diagonal para captura

        return False
