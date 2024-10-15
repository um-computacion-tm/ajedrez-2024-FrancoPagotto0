from piece import Piece

class Queen(Piece):
    white_str = "♛"
    black_str = "♕"
    
    def __init__(self, color, board):
        super().__init__(color, board)
    
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
        possible_positions = self.possible_moves(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions

    
        