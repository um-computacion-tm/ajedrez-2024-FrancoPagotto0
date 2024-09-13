from chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)
        
def play(chess):
    try:
        print(chess.show_board())
        print("Turno: ", chess.turn)
        try:
            from_row = int(input("Desde Fila: "))
            from_col = int(input("Desde Columna: "))
            to_row = int(input("A Fila: "))
            to_col = int(input("A Columna: "))
        except ValueError:
          print("Ingrese un número válido para filas y columnas.")
          return

        chess.move(
          from_row,
          from_col,
          to_row,
          to_col,
          )
    except InvalidMove as e:
        print(e)
    except InvalidTurn as e:
        print(e)
    except EmptyPosition as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
if __name__ == '__main__':
    main()
