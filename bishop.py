from piece import Piece

from piece import Piece

class Bishop(Piece):
    white_str = "♝"
    black_str = "♗"

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        directions = [
            (1, 1),   # Down-Right
            (1, -1),  # Down-Left
            (-1, 1),  # Up-Right
            (-1, -1)  # Up-Left
        ]
        possible_positions = self.possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions