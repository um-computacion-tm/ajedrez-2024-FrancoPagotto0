class Piece:
    def __init__(self, color,board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        return self.__color__
    
    def possible_moves(self, from_row, from_col, directions, single_step=False):
        moves = []
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    destination_piece = self.__board__.get_piece(new_row, new_col)
                    if destination_piece is None:
                        moves.append((new_row, new_col))
                    elif destination_piece.get_color() != self.get_color():
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break
            
                if single_step:
                    break
        return moves

  