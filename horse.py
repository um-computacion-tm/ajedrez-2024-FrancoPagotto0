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
        possible_positions = (
            self.possible_positions_up_right(from_row, from_col) +   
            self.possible_positions_up_left(from_row, from_col) +    
            self.possible_positions_down_right(from_row, from_col) + 
            self.possible_positions_down_left(from_row, from_col)    
        )
        return (to_row, to_col) in possible_positions

    def possible_positions_up_right(self, row, col):
        possibles = []
        horse_moves = [(2, 1), (1, 2)]  
        for move in horse_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        return possibles

    def possible_positions_up_left(self, row, col):
        possibles = []
        horse_moves = [(2, -1), (1, -2)]  
        for move in horse_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        return possibles

    def possible_positions_down_right(self, row, col):
        possibles = []
        horse_moves = [(-2, 1), (-1, 2)]
        for move in horse_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        return possibles

    def possible_positions_down_left(self, row, col):
        possibles = []
        horse_moves = [(-2, -1), (-1, -2)]  
        for move in horse_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        return possibles


   
