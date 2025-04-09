import sqlite3

class SQL:
    """
    Clase para manejar operaciones básicas con SQLite.
    """
    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    def ejecutar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()

    def consultar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar(self):
        self.conexion.close()

    def crear_tabla(self, tabla, columnas):
        """
        Crea una tabla en la base de datos.
        :param tabla: Nombre de la tabla.
        :param columnas: Definición de las columnas (ejemplo: "id INTEGER PRIMARY KEY, nombre TEXT").
        """
        consulta = f"CREATE TABLE IF NOT EXISTS {tabla} ({columnas})"
        self.ejecutar(consulta)

    def insertar(self, tabla, columnas, valores):
        """
        Inserta un registro en la tabla.
        :param tabla: Nombre de la tabla.
        :param columnas: Columnas donde se insertarán los valores (ejemplo: "nombre, edad").
        :param valores: Valores a insertar como tupla.
        """
        marcadores = ", ".join(["?"] * len(valores))
        consulta = f"INSERT INTO {tabla} ({columnas}) VALUES ({marcadores})"
        self.ejecutar(consulta, valores)

    def obtener_todos(self, tabla):
        """
        Recupera todos los registros de una tabla.
        :param tabla: Nombre de la tabla.
        :return: Lista de registros.
        """
        consulta = f"SELECT * FROM {tabla}"
        return self.consultar(consulta)
