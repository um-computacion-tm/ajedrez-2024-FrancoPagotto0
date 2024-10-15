from rook import Rook
from horse import Horse
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from exceptions import OutOfBoard, InvalidMove, EmptyPosition, CaptureOwnPieceError

class Board:    
    def __init__(self, for_test = False):
       self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
       if not for_test:
            self.__positions__[0][0] = Rook("BLACK",self)
            self.__positions__[0][7] = Rook("BLACK",self)
            self.__positions__[7][7] = Rook("WHITE",self)
            self.__positions__[7][0] = Rook("WHITE",self)

      
            self.__positions__[0][1] = Horse("BLACK", self)
            self.__positions__[0][6] = Horse("BLACK", self)
            self.__positions__[7][1] = Horse("WHITE", self)
            self.__positions__[7][6] = Horse("WHITE", self)

            self.__positions__[0][2] = Bishop("BLACK", self)
            self.__positions__[0][5] = Bishop("BLACK", self)
            self.__positions__[7][2] = Bishop("WHITE", self)
            self.__positions__[7][5] = Bishop("WHITE", self)

            self.__positions__[0][3] = Queen("BLACK", self)
            self.__positions__[7][3] = Queen("WHITE", self)

            self.__positions__[0][4] = King("BLACK", self)
            self.__positions__[7][4] = King("WHITE", self)

            for col in range(8):
                self.__positions__[1][col] = Pawn("BLACK", self)
                self.__positions__[6][col] = Pawn("WHITE", self)

          
    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise OutOfBoard()

    def set_piece(self, row, col, piece):
        if 0 <= row < 8 and 0 <= col < 8:
            self.__positions__[row][col] = piece
            if piece:
                piece.set_position(row, col)
        else:
            raise OutOfBoard()

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        
        if not origin:
            raise EmptyPosition()
        
        if not origin.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        
        destination = self.get_piece(to_row, to_col)
    
        if destination is not None and destination.get_color() == origin.get_color():
            raise CaptureOwnPieceError()
        
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

        
    def print_board(self):
        for row in self.__positions__:
            print(" ".join([str(piece) if piece else "." for piece in row]))
        print()
    