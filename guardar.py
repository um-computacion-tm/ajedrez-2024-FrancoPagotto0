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


#____________________________________________________________________________________________