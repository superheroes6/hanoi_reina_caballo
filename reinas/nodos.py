class NodoReina:

    def __init__(self, tablero):
        self.tablero = tablero
        self.soluciones = []

    def agregar_solucion(self, solucion):
        self.soluciones.append(solucion)

    def __repr__(self):
        return f"NodoReina({self.tablero})"
