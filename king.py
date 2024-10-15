from piece import Piece

class King(Piece):
    white_str = "♚"
    black_str = "♔"

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        directions = [
            (1, 0), (0, 1), (0, -1), (-1, 0),  # Vertical and Horizontal
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonals
        ]
        possible_positions = self.possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

  
    
