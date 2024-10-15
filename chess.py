from board import Board
from exceptions import EmptyPosition, InvalidTurn, InvalidMove

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        
    def get_board(self):
        return self.__board__
    def move(self, start_x, start_y, end_x, end_y):
        piece = self.__board__.get_piece(start_x, start_y)
        
        if not piece:
            raise EmptyPosition("La posición está vacía")
        if piece.get_color() != self.__turn__:
            raise EmptyPosition("No puedes mover pieza de otro jugador")
        if not piece.valid_positions(start_x, start_y, end_x, end_y):
            raise InvalidMove("Movimiento inválido")
        
        
        
        
        self.__board__.move(start_x, start_y, end_x, end_y)
        self.change_turn()

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
    
    def get_turn(self):
        return self.__turn__