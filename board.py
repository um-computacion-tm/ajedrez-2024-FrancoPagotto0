from piece import Rook

class Board:
    def __init__(self):
        self.position = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.position.append(col)
        self.position[0][0] = Rook("BLACK")
        self.position[0][7] = Rook("BLACK")
        self.position[7][7] = Rook("WHITE")
        self.position[7][0] = Rook("WHITE")
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]