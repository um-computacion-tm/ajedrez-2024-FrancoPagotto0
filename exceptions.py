class InvalidMove(Exception):
    message = "Movimieto invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"
    
class MoveForwardError(InvalidMove):
    message = "El peón no puede capturar hacia adelante"

class PathOccupiedError(InvalidMove):
    message = "Hay piezas en el camino"

class CaptureOwnPieceError(InvalidMove):
    message = "No puedes capturar una pieza de tu propio color"
    
class GameOver(Exception):  
    message = "Fin del juego. ¡Gracias por jugar!"
    
    def __init__(self, message):
        self.__message__ = message
        super().__init__(message)