import sqlite3

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

def hanoi(n, source, target, auxiliary):

    if n == 1:
        return [(source, target)]
    moves = hanoi(n - 1, source, auxiliary, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, auxiliary, target, source))
    return moves