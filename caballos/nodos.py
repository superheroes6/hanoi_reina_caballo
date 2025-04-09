class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []

    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)

    def __repr__(self):
        return f"Nodo({self.valor})"
