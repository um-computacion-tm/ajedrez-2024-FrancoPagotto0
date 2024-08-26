from piece import Piece

class Horse(Piece):
    def __str__(self):
        if self.color == "WHITE":
            return "♞"
        else:
            return "♘"
 
   
