import sqlite3
from hanoi.hanoi import hanoi
from caballos.caballos import knight_moves_count
from reinas.reinas import solve_n_queens

class SQL:

    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def ejecutar(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def consultar(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def cerrar(self):
        self.connection.close()

if __name__ == "__main__":
    print("Movimientos de Hanoi:", hanoi(3, 'A', 'C', 'B'))
    print("Movimientos válidos del caballo:", knight_moves_count(2))
    print("Soluciones para las n-reinas:", solve_n_queens(4))
