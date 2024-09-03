from rook import Rook

class Board:
    def __init__(self, for_test = False):
        self.__position__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__position__.append(col)
        if not for_test:
            self.__position__[0][0] = Rook("BLACK",self)
            self.__position__[0][7] = Rook("BLACK",self)
            self.__position__[7][7] = Rook("WHITE",self)
            self.__position__[7][0] = Rook("WHITE",self)

    def __str__(self):
        board_str = ""
        for row in self.__position__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):
        return self.__position__[row][col]
   
    def set_piece(self, row, col, piece):
        self.__position__[row][col] = piece