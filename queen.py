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
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col) +
            self.possible_positions_hd(from_row, from_col) +
            self.possible_positions_ha(from_row, from_col) +
            self.possible_positions_dd(from_row, from_col) +
            self.possible_positions_da(from_row, from_col) +
            self.possible_positions_id(from_row, from_col) +
            self.possible_positions_ia(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    # Vertical abajo
    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    # Vertical arriba
    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    # Horizontal derecha
    def possible_positions_hd(self, row, col):
        possibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles

    # Horizontal izq
    def possible_positions_ha(self, row, col):
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles

    # Diagonal abajo-derecha
    def possible_positions_dd(self, row, col):
        possibles = []
        next_row, next_col = row + 1, col + 1
        while next_row < 8 and next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row += 1
            next_col += 1
        return possibles

    # Diagonal abajo izq
    def possible_positions_da(self, row, col):
        possibles = []
        next_row, next_col = row + 1, col - 1
        while next_row < 8 and next_col >= 0:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row += 1
            next_col -= 1
        return possibles

    # Diagonal arriba derecha
    def possible_positions_id(self, row, col):
        possibles = []
        next_row, next_col = row - 1, col + 1
        while next_row >= 0 and next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col += 1
        return possibles

    # Diagonal aribba izq
    def possible_positions_ia(self, row, col):
        possibles = []
        next_row, next_col = row - 1, col - 1
        while next_row >= 0 and next_col >= 0:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col -= 1
        return possibles

