from chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition, GameOver

def play(chess):
    while True:
        try:
            from_row = input("De Fila (o 'EXIT' para salir): ")
            if from_row.upper() == "EXIT":
                raise GameOver(GameOver.message)

            from_col = input("De Columna (o 'EXIT' para salir): ")
            if from_col.upper() == "EXIT":
                raise GameOver(GameOver.message)

            to_row = input("A Fila (o 'EXIT' para salir): ")
            if to_row.upper() == "EXIT":
                raise GameOver(GameOver.message)

            to_col = input("A Columna (o 'EXIT' para salir): ")
            if to_col.upper() == "EXIT":
                raise GameOver(GameOver.message)

            from_row = int(from_row)
            from_col = int(from_col)
            to_row = int(to_row)
            to_col = int(to_col)

            chess.move(from_row, from_col, to_row, to_col)
            chess.get_board().print_board()  # Imprimir el tablero después de cada movimiento

        except ValueError:
            print("Entrada inválida. Por favor, introduce números válidos.")
        except InvalidMove:
            print("Movimiento inválido. Inténtalo de nuevo.")
        except InvalidTurn:
            print("No es tu turno. Espera tu turno.")
        except EmptyPosition:
            print("No hay pieza en la posición especificada. Inténtalo de nuevo.")
        except GameOver as e:
            print(str(e))
            break

def main():
    chess = Chess()
    chess.get_board().print_board()  #
    play(chess)

if __name__ == "__main__":
    main()  