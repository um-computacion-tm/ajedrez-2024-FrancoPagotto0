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
        possible_positions = (
            self.possible_positions_vertical(from_row, from_col) +
            self.possible_positions_horizontal(from_row, from_col) +
            self.possible_positions_diagonal(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def possible_positions_vertical(self, row, col):
        possibles = []
        for direction in [1, -1]:  # Movimientos hacia arriba y abajo
            next_row = row + direction
            if 0 <= next_row < 8:
                other_piece = self.__board__.get_piece(next_row, col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((next_row, col))
        return possibles

    def possible_positions_horizontal(self, row, col):
        possibles = []
        for direction in [1, -1]:  # Movimientos hacia la derecha y la izquierda
            next_col = col + direction
            if 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(row, next_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((row, next_col))
        return possibles

    def possible_positions_diagonal(self, row, col):
        possibles = []
        for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:  # Movimientos diagonales
            next_row = row + direction[0]
            next_col = col + direction[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((next_row, next_col))
        return possibles
