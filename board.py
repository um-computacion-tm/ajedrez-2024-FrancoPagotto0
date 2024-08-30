from rook import Rook
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from queen import Queen


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
        
         # Posición inicial Horse
        self.position[0][1] = Horse("BLACK")
        self.position[0][6] = Horse("BLACK")
        self.position[7][1] = Horse("WHITE")
        self.position[7][6] = Horse("WHITE")
        # Posición inicial bishop
        self.position[0][2] = Bishop("BLACK")
        self.position[0][5] = Bishop("BLACK")
        self.position[7][2] = Bishop("WHITE")
        self.position[7][5] = Bishop("WHITE")

        # Posición inicial Queen
        self.position[0][3] = Queen("BLACK")
        self.position[7][3] = Queen("WHITE")



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