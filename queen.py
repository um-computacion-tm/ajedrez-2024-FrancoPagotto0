from piece import Piece

class Queen(Piece):
    white_str = "♛"
    black_str = "♕"
    
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

    def possible_moves(self, from_row, from_col, directions, single_step=False):
        moves = []
        for dr, dc in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += dr
                new_col += dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                    if single_step:
                        break
                else:
                    break
        return moves