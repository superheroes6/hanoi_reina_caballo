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

class NodoHanoi:

    def __init__(self, torres):
        self.torres = torres
        self.movimientos = []

    def agregar_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

    def __repr__(self):
        return f"NodoHanoi({self.torres})"
