from rook import Rook
from horse import Horse
from bishop import Bishop
from exceptions import OutOfBoard, InvalidMove

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

      
            self.__position__[0][1] = Horse("BLACK", self)
            self.__position__[0][6] = Horse("BLACK", self)
            self.__position__[7][1] = Horse("WHITE", self)
            self.__position__[7][6] = Horse("WHITE", self)

            self.__position__[0][2] = Bishop("BLACK", self)
            self.__position__[0][5] = Bishop("BLACK", self)
            self.__position__[7][2] = Bishop("WHITE", self)
            self.__position__[7][5] = Bishop("WHITE", self)

          
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
        if not ( 0 <= row < 8 or 0 <= col < 8):
            raise OutOfBoard()
        return self.__position__[row][col]
    
    def set_piece(self, row, col, piece):
        if not (0 <= row < 8 and 0 <= col < 8):
            raise OutOfBoard()
        self.__position__[row][col] = piece
    
    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        destination = self.get_piece(to_row, to_col)
        
        if destination is not None and destination.get_color() == origin.get_color():
            raise InvalidMove("No puedes tomar una pieza de tu mismo color")
        
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)