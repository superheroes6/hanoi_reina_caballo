import tkinter as tk
from tkinter import ttk
import random
import time

class RecorridoCaballoApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.canvas = tk.Canvas(raiz, width=400, height=400)
        self.canvas.pack()
        self.tamaño_tablero = 8
        self.posicion_caballo = (0, 0)
        self.visitado = [[False] * self.tamaño_tablero for _ in range(self.tamaño_tablero)]
        self.crear_controles()

    def crear_controles(self):
        marco_controles = tk.Frame(self.raiz)
        marco_controles.pack()

        tk.Button(
            marco_controles, text="Iniciar Recorrido",
            command=self.iniciar_recorrido
        ).pack(side=tk.LEFT)

    def dibujar_tablero(self):
        self.canvas.delete("all")
        for fila in range(self.tamaño_tablero):
            for columna in range(self.tamaño_tablero):
                color = "white" if (fila + columna) % 2 == 0 else "gray"
                x1, y1 = columna * 50, fila * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                if self.visitado[fila][columna]:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")

    def dibujar_caballo(self):
        x, y = self.posicion_caballo
        x1, y1 = y * 50 + 10, x * 50 + 10
        x2, y2 = x1 + 30, y1 + 30
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", tags="caballo")

    def es_movimiento_valido(self, x, y):
        return 0 <= x < self.tamaño_tablero and 0 <= y < self.tamaño_tablero and not self.visitado[x][y]

    def recorrido_caballo(self, x, y, contador_movimientos):
        if contador_movimientos == self.tamaño_tablero * self.tamaño_tablero:
            return True

        movimientos = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2),
            (2, 1), (2, -1), (1, -2), (-1, -2)
        ]
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if self.es_movimiento_valido(nx, ny):
                self.visitado[nx][ny] = True
                self.posicion_caballo = (nx, ny)
                self.dibujar_tablero()
                self.dibujar_caballo()
                self.raiz.update()
                time.sleep(0.3)
                if self.recorrido_caballo(nx, ny, contador_movimientos + 1):
                    return True
                self.visitado[nx][ny] = False
        return False

    def iniciar_recorrido(self):
        self.posicion_caballo = (random.randint(0, self.tamaño_tablero - 1), random.randint(0, self.tamaño_tablero - 1))
        self.visitado = [[False] * self.tamaño_tablero for _ in range(self.tamaño_tablero)]
        x, y = self.posicion_caballo
        self.visitado[x][y] = True
        self.dibujar_tablero()
        self.dibujar_caballo()
        if not self.recorrido_caballo(x, y, 1):
            print("No se encontró solución.")

class HanoiApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.canvas = tk.Canvas(raiz, width=600, height=400)
        self.canvas.pack()
        self.num_discos = 0
        self.varillas = [[], [], []]
        self.ancho_discos = []
        self.crear_controles()

    def crear_controles(self):
        marco_controles = tk.Frame(self.raiz)
        marco_controles.pack()

        tk.Label(marco_controles, text="Número de Discos:").pack(side=tk.LEFT)
        self.entrada_discos = tk.Entry(marco_controles, width=5)
        self.entrada_discos.pack(side=tk.LEFT)

        tk.Button(
            marco_controles, text="Iniciar",
            command=self.iniciar_hanoi
        ).pack(side=tk.LEFT)

    def dibujar_varillas(self):
        self.canvas.delete("all")
        for i in range(3):
            x = 150 + i * 200
            self.canvas.create_line(x, 100, x, 300, width=5)
        self.canvas.create_line(50, 300, 550, 300, width=5)

    def dibujar_discos(self):
        self.canvas.delete("disco")
        for indice_varilla, varilla in enumerate(self.varillas):
            x_centro = 150 + indice_varilla * 200
            for nivel, disco in enumerate(varilla):
                ancho = self.ancho_discos[disco - 1]
                x1 = x_centro - ancho // 2
                x2 = x_centro + ancho // 2
                y1 = 300 - (nivel + 1) * 20
                y2 = y1 + 20
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="disco")

    def mover_disco(self, desde_varilla, hacia_varilla):
        disco = self.varillas[desde_varilla].pop()
        self.varillas[hacia_varilla].append(disco)
        self.dibujar_discos()
        self.raiz.update()
        time.sleep(0.5)

    def hanoi(self, n, desde_varilla, hacia_varilla, varilla_auxiliar):
        if n == 1:
            self.mover_disco(desde_varilla, hacia_varilla)
        else:
            self.hanoi(n - 1, desde_varilla, varilla_auxiliar, hacia_varilla)
            self.mover_disco(desde_varilla, hacia_varilla)
            self.hanoi(n - 1, varilla_auxiliar, hacia_varilla, desde_varilla)

    def iniciar_hanoi(self):
        try:
            self.num_discos = int(self.entrada_discos.get())
            if self.num_discos <= 0:
                raise ValueError("El número de discos debe ser positivo.")
            self.varillas = [list(range(self.num_discos, 0, -1)), [], []]
            self.ancho_discos = [30 + i * 20 for i in range(self.num_discos)]
            self.dibujar_varillas()
            self.dibujar_discos()
            self.hanoi(self.num_discos, 0, 2, 1)
        except ValueError:
            print("Por favor, ingrese un número positivo válido.")

class NReinasApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.canvas = tk.Canvas(raiz, width=400, height=400)
        self.canvas.pack()
        self.n = 0
        self.tablero = []
        self.crear_controles()

    def crear_controles(self):
        marco_controles = tk.Frame(self.raiz)
        marco_controles.pack()

        tk.Label(marco_controles, text="Número de Reinas:").pack(side=tk.LEFT)
        self.entrada_reinas = tk.Entry(marco_controles, width=5)
        self.entrada_reinas.pack(side=tk.LEFT)

        tk.Button(
            marco_controles, text="Resolver",
            command=self.iniciar_nreinas
        ).pack(side=tk.LEFT)

    def dibujar_tablero(self):
        self.canvas.delete("all")
        tamaño_celda = 400 // self.n
        for fila in range(self.n):
            for columna in range(self.n):
                color = "white" if (fila + columna) % 2 == 0 else "gray"
                x1, y1 = columna * tamaño_celda, fila * tamaño_celda
                x2, y2 = x1 + tamaño_celda, y1 + tamaño_celda
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def dibujar_reinas(self):
        self.canvas.delete("reina")
        tamaño_celda = 400 // self.n
        for fila in range(self.n):
            for columna in range(self.n):
                if self.tablero[fila][columna] == 1:
                    x1 = columna * tamaño_celda + tamaño_celda // 4
                    y1 = fila * tamaño_celda + tamaño_celda // 4
                    x2 = x1 + tamaño_celda // 2
                    y2 = y1 + tamaño_celda // 2
                    self.canvas.create_oval(x1, y1, x2, y2, fill="red", tags="reina")

    def es_seguro(self, fila, columna):
        for i in range(fila):
            if self.tablero[i][columna] == 1:
                return False
        for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
            if self.tablero[i][j] == 1:
                return False
        for i, j in zip(range(fila, -1, -1), range(columna, self.n)):
            if self.tablero[i][j] == 1:
                return False
        return True

    def resolver_nreinas(self, fila):
        if fila == self.n:
            return True
        for columna in range(self.n):
            if self.es_seguro(fila, columna):
                self.tablero[fila][columna] = 1
                self.dibujar_reinas()
                self.raiz.update()
                if self.resolver_nreinas(fila + 1):
                    return True
                self.tablero[fila][columna] = 0
                self.dibujar_reinas()
                self.raiz.update()
        return False

    def iniciar_nreinas(self):
        try:
            self.n = int(self.entrada_reinas.get())
            if self.n <= 0:
                raise ValueError("El número de reinas debe ser positivo.")
            self.tablero = [[0] * self.n for _ in range(self.n)]
            self.dibujar_tablero()
            if not self.resolver_nreinas(0):
                print("No existe solución.")
        except ValueError:
            print("Por favor, ingrese un número positivo válido.")

class AplicacionPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Aplicaciones Combinadas")
        self.notebook = ttk.Notebook(raiz)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña Recorrido del Caballo
        marco_caballo = tk.Frame(self.notebook)
        self.notebook.add(marco_caballo, text="Recorrido del Caballo")
        RecorridoCaballoApp(marco_caballo)

        # Pestaña Torre de Hanoi
        marco_hanoi = tk.Frame(self.notebook)
        self.notebook.add(marco_hanoi, text="Torre de Hanoi")
        HanoiApp(marco_hanoi)

        # Pestaña N-Reinas
        marco_reinas = tk.Frame(self.notebook)
        self.notebook.add(marco_reinas, text="N-Reinas")
        NReinasApp(marco_reinas)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = AplicacionPrincipal(raiz)
    raiz.mainloop()