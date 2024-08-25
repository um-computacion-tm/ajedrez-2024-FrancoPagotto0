from rook import Rook
from pawn import Pawn

class Board:
    def __init__(self):
        self.position = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.position.append(col)
        # Posicion inicial Rook
        self.position[0][0] = Rook("BLACK")
        self.position[0][7] = Rook("BLACK")
        self.position[7][7] = Rook("WHITE")
        self.position[7][0] = Rook("WHITE")

         # Posición inicial Pawn
        for i in range(8):
            self.position[1][i] = Pawn("WHITE") 
            self.position[6][i] = Pawn("BLACK") 


    def __str__(self):
        board_str = ""
        for row in self.position:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):
        return self.position[row][col]