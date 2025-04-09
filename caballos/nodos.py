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

class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []

    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)

    def __repr__(self):
        return f"Nodo({self.valor})"
