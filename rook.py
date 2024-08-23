from piece import Piece

class Rook(Piece):
    def __str__(self):
        if self.color == "WHITE":
            return "♜"
        else:
            return "♖"

