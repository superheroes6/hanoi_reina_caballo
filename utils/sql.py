import sqlite3

class SQL:
    """
    Clase para manejar operaciones básicas con SQLite.
    """
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

    def crear_tabla(self, tabla, columnas):
        """
        Crea una tabla en la base de datos.
        :param tabla: Nombre de la tabla.
        :param columnas: Definición de las columnas (ejemplo: "id INTEGER PRIMARY KEY, name TEXT").
        """
        query = f"CREATE TABLE IF NOT EXISTS {tabla} ({columnas})"
        self.ejecutar(query)

    def insertar(self, tabla, columnas, valores):
        """
        Inserta un registro en la tabla.
        :param tabla: Nombre de la tabla.
        :param columnas: Columnas donde se insertarán los valores (ejemplo: "name, age").
        :param valores: Valores a insertar como tupla.
        """
        placeholders = ", ".join(["?"] * len(valores))
        query = f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})"
        self.ejecutar(query, valores)

    def obtener_todos(self, tabla):
        """
        Recupera todos los registros de una tabla.
        :param tabla: Nombre de la tabla.
        :return: Lista de registros.
        """
        query = f"SELECT * FROM {tabla}"
        return self.consultar(query)
