from piece import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"
      
    def valid_positions(self, from_row, from_col, to_row, to_col):
        directions = [
            (1, 0),   # Down
            (-1, 0),  # Up
            (0, 1),   # Right
            (0, -1)   # Left
        ]
        possible_positions = self.possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def possible_moves(self, from_row, from_col, directions):
        # Implement the logic to calculate possible moves for the Rook
        possible_positions = []
        for direction in directions:
            for i in range(1, 8):  # Assuming an 8x8 chess board
                new_row = from_row + direction[0] * i
                new_col = from_col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:  # Check if within bounds
                    possible_positions.append((new_row, new_col))
                else:
                    break
        return possible_positions