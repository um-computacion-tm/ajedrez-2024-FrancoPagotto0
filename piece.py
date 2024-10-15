class Piece:
    def __init__(self, color, board):
        self.__color = color
        self.__board = board
        self.__row = None
        self.__col = None

    def get_color(self):
        return self.__color

    def get_board(self):
        return self.__board

    def set_position(self, row, col):
        self.__row = row
        self.__col = col

    def is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def possible_moves(self, row, col, directions, single_step=False):
        moves = []
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            while self.is_within_board(new_row, new_col):
                piece = self.__board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))
                elif piece.get_color() != self.__color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                if single_step:
                    break
                new_row += direction[0]
                new_col += direction[1]
        return moves

    def valid_positions(self):
        raise NotImplementedError("This method should be overridden in subclasses")
  