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
        possible_positions = (
            self.possible_positions_dd(from_row, from_col) +  
            self.possible_positions_da(from_row, from_col) +  
            self.possible_positions_id(from_row, from_col) +  
            self.possible_positions_ia(from_row, from_col)   
        )
        return (to_row, to_col) in possible_positions

    def possible_positions_dd(self, row, col):
        possibles = []
        for offset in range(1, 8):
            new_row = row + offset
            new_col = col + offset
            if new_row >= 8 or new_col >= 8:
                break
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
                break
            possibles.append((new_row, new_col))
        return possibles

    def possible_positions_da(self, row, col):
        possibles = []
        for offset in range(1, 8):
            new_row = row + offset
            new_col = col - offset
            if new_row >= 8 or new_col < 0:
                break
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
                break
            possibles.append((new_row, new_col))
        return possibles

    def possible_positions_id(self, row, col):
        possibles = []
        for offset in range(1, 8):
            new_row = row - offset
            new_col = col + offset
            if new_row < 0 or new_col >= 8:
                break
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
                break
            possibles.append((new_row, new_col))
        return possibles

    def possible_positions_ia(self, row, col):
        possibles = []
        for offset in range(1, 8):
            new_row = row - offset
            new_col = col - offset
            if new_row < 0 or new_col < 0:
                break
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
                break
            possibles.append((new_row, new_col))
        return possibles
