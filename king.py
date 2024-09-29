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

    def possible_moves(self, from_row, from_col, directions):
        moves = []
        for dr, dc in directions:
            new_row, new_col = from_row + dr, from_col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))
        return moves
