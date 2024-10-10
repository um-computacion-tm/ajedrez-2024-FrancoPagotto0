from piece import Piece

class Horse(Piece):
    white_str = "♞"
    black_str = "♘"

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):                     
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),  # Movimientos en L hacia arriba y hacia abajo
            (1, 2), (1, -2), (-1, 2), (-1, -2)  # Movimientos en L hacia los lados
        ]
        possible_positions = self.possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    
        
