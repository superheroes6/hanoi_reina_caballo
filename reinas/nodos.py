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

class NodoReina:

    def __init__(self, tablero):
        self.tablero = tablero
        self.soluciones = []

    def agregar_solucion(self, solucion):
        self.soluciones.append(solucion)

    def __repr__(self):
        return f"NodoReina({self.tablero})"
