from board import Board
from exceptions import InvalidMove, InvalidTurn, EmptyPosition
 
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        
    def get_board(self):
        return self.__board__

    def move(self, from_row, from_col, to_row, to_col):
        
        try:
            piece = self.__board__.get_piece(from_row, from_col)

            if not piece:
                raise EmptyPosition() 
            if piece.get_color() != self.__turn__:
                raise InvalidTurn() 
            if not piece.valid_positions(from_row, from_col, to_row, to_col):
                raise InvalidMove()  
            self.__board__.move(from_row, from_col, to_row, to_col)
            self.change_turn()

        except (EmptyPosition, InvalidMove, InvalidTurn) as e:
           print(str(e)) 
    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"