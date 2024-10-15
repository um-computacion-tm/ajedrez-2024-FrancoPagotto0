from piece import Piece

class Bishop(Piece):
    white_str = "♝"
    black_str = "♗"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Check if the move is diagonal
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        
        # Check if the destination is within the board
        if not self.is_within_board(to_row, to_col):
            return False
        
        # Determine the direction of the move
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        
        # Check each square along the diagonal path
        current_row, current_col = from_row + row_step, from_col + col_step
        while current_row != to_row and current_col != to_col:
            if self.get_board().get_piece(current_row, current_col) is not None:
                return False
            current_row += row_step
            current_col += col_step
        
        # Check the destination square
        destination_piece = self.get_board().get_piece(to_row, to_col)
        if destination_piece is None or destination_piece.get_color() != self.get_color():
          
          
         def __str__(self):
           return self.white_str if self.get_color() == "WHITE" else self.black_str
        
       