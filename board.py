from rook import Rook
from horse import Horse
from queen import Queen
from bishop import Bishop
from king import King
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

        # Posicion inicial Horse
        self.position[0][1] = Horse("BLACK")
        self.position[0][6] = Horse("BLACK")
        self.position[7][1] = Horse("WHITE")
        self.position[7][6] = Horse("WHITE")

        #Posicion inicial Bishop
 
        self.position[0][2] = Bishop("BLACK")
        self.position[0][5] = Bishop("BLACK")
        self.position[7][2] = Bishop("WHITE")
        self.position[7][5] = Bishop("WHITE")

        # Posicion inicial Queen
        self.position[0][3] = Queen("BLACK")
        self.position[7][3] = Queen("WHITE")

        # Posicion inicial King
        self.position[0][4] = King("BLACK")
        self.position[7][4] = King("WHITE")

        # Posicion inicial Pawn
        for i in range(8):
            self.position[1][i] = Pawn("BLACK")
            self.position[6][i] = Pawn("WHITE")
    
    def get_piece(self, row, col):
        return self.position[row][col]