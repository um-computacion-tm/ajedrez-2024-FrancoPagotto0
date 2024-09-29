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

    def possible_moves(self, from_row, from_col, directions):
        moves = []
        for dr, dc in directions:
            new_row, new_col = from_row + dr, from_col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                destination_piece = self.__board__.get_piece(new_row, new_col)
                # Agregar solo posiciones vacías o ocupadas por piezas del oponente
                if destination_piece is None or destination_piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))
        return moves
