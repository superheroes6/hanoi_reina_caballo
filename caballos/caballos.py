import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def contar_movimientos_caballo(movimientos):

    teclado = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    def dfs(posicion, movimientos_restantes):
        if movimientos_restantes == 0:
            return 1
        return sum(dfs(siguiente, movimientos_restantes - 1) for siguiente in teclado[posicion])

    total_movimientos = 0
    for inicio in range(10):
        total_movimientos += dfs(inicio, movimientos)
    return total_movimientos

def mostrar_resultado_movimientos_caballo():
    movimientos = int(entrada_movimientos.get())
    ruta_imagen = f"images/knight_moves_{movimientos}.png"
    try:
        img = Image.open(ruta_imagen)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        etiqueta_imagen.config(image=img_tk)
        etiqueta_imagen.image = img_tk
    except FileNotFoundError:
        etiqueta_imagen.config(text=f"No se encontró la imagen para {movimientos} movimientos en '{ruta_imagen}'.")

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Movimientos del Caballo")

# Entradas
ttk.Label(raiz, text="Número de movimientos:").grid(row=0, column=0, padx=5, pady=5)
entrada_movimientos = ttk.Entry(raiz)
entrada_movimientos.grid(row=0, column=1, padx=5, pady=5)
entrada_movimientos.insert(0, "2")

# Botón para calcular
boton_calcular = ttk.Button(raiz, text="Mostrar movimientos", command=mostrar_resultado_movimientos_caballo)
boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar la imagen
etiqueta_imagen = ttk.Label(raiz)
etiqueta_imagen.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
raiz.mainloop()

