from piece import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"
      
    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        
        directions = [
            (1, 0),   # Down
            (-1, 0),  # Up
            (0, 1),   # Right
            (0, -1)   # Left
        ]
        possible_positions = self.possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions