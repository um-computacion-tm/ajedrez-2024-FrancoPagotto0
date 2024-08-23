import pygame
import sys

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
size = (480, 480)
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("Ajedrez")

# Colores
COLOR_CLARO = (240, 217, 181)  # Color claro del tablero
COLOR_OSCURO = (181, 136, 99)  # Color oscuro del tablero
COLOR_FONDO = (255, 255, 255)  # Blanco para el fondo de la pantalla
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
COLOR_INDICADOR = (255, 0, 0)  # Rojo para resaltar casillas capturables

class Piece:
    def __init__(self, color):
        self.color = color

    def draw(self, surface, x, y):
        raise NotImplementedError("Debe implementarse en una subclase")

class Rook(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class Knight(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class Bishop(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class Queen(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class King(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class Pawn(Piece):
    def draw(self, surface, x, y):
        pygame.draw.circle(surface, NEGRO if self.color == "black" else BLANCO, (x + 30, y + 30), 20)

class Board:
    def __init__(self):
        self.position = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Colocar las piezas en sus posiciones iniciales
        for i in [0, 7]:
            self.position[i][0] = Rook("black" if i == 0 else "white")
            self.position[i][7] = Rook("black" if i == 0 else "white")
        for i in [0, 7]:
            self.position[i][1] = Knight("black" if i == 0 else "white")
            self.position[i][6] = Knight("black" if i == 0 else "white")
        for i in [0, 7]:
            self.position[i][2] = Bishop("black" if i == 0 else "white")
            self.position[i][5] = Bishop("black" if i == 0 else "white")
        self.position[0][3] = Queen("black")
        self.position[0][4] = King("black")
        self.position[7][3] = Queen("white")
        self.position[7][4] = King("white")
        for i in range(8):
            self.position[1][i] = Pawn("black")
            self.position[6][i] = Pawn("white")

    def get_piece(self, row, col):
        return self.position[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece:
            self.position[to_row][to_col] = piece
            self.position[from_row][from_col] = None

    def get_capture_positions(self, row, col, color):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        captures = []
        piece = self.get_piece(row, col)
        if piece:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = self.get_piece(r, c)
                    if target and target.color != color:
                        captures.append((r, c))
        return captures

    def dibujar(self, pantalla, selected_row=None, selected_col=None):
        # Dibujar el tablero
        for fila in range(8):
            for columna in range(8):
                color = COLOR_CLARO if (fila + columna) % 2 == 0 else COLOR_OSCURO
                pygame.draw.rect(pantalla, color, pygame.Rect(columna * 60, fila * 60, 60, 60))
                
                pieza = self.get_piece(fila, columna)
                if pieza:
                    pieza.draw(pantalla, columna * 60, fila * 60)

                # Si se ha seleccionado una pieza, resaltar las casillas donde puede capturar
                if selected_row is not None and selected_col is not None:
                    pieza = self.get_piece(selected_row, selected_col)
                    if pieza:
                        captures = self.get_capture_positions(selected_row, selected_col, pieza.color)
                        if (fila, columna) in captures:
                            pygame.draw.rect(pantalla, COLOR_INDICADOR, pygame.Rect(columna * 60, fila * 60, 60, 60), 5)

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.selected_piece = None
        self.selected_pos = None

    def select_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected_piece = piece
            self.selected_pos = (row, col)

    def move(self, to_row, to_col):
        if self.selected_piece:
            from_row, from_col = self.selected_pos
            # Simplificación: mueve la pieza sin verificar reglas avanzadas
            self.board.move_piece(from_row, from_col, to_row, to_col)
            self.change_turn()
            self.selected_piece = None
            self.selected_pos = None

    def change_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

# Crear una instancia del juego de ajedrez
chess_game = Chess()

# Bucle principal de Pygame
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // 60
            row = y // 60
            if chess_game.selected_piece:
                chess_game.move(row, col)
            else:
                chess_game.select_piece(row, col)
    
    # Rellenar la pantalla con el color de fondo y dibujar el tablero
    pantalla.fill(COLOR_FONDO)
    chess_game.board.dibujar(pantalla, chess_game.selected_pos[0] if chess_game.selected_pos else None, chess_game.selected_pos[1] if chess_game.selected_pos else None)
    
    pygame.display.flip()
