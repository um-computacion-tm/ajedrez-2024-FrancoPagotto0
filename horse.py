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
        possible_positions = self.possible_positions_horse(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_positions_horse(self, row, col):
        possibles = []
        # Movimientos del caballo (en forma de "L")
        horse_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in horse_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Dentro del tablero
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        
        return possibles

   
