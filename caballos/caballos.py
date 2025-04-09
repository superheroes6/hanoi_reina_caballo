import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def knight_moves_count(moves):

    keypad = {
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

    def dfs(position, remaining_moves):
        if remaining_moves == 0:
            return 1
        return sum(dfs(next_pos, remaining_moves - 1) for next_pos in keypad[position])

    total_moves = 0
    for start in range(10):
        total_moves += dfs(start, moves)
    return total_moves

def show_knight_moves_result():
    moves = int(entry_moves.get())
    image_path = f"images/knight_moves_{moves}.png"
    try:
        img = Image.open(image_path)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        label_image.config(image=img_tk)
        label_image.image = img_tk
    except FileNotFoundError:
        label_image.config(text=f"No se encontró la imagen para {moves} movimientos en '{image_path}'.")

# Crear la ventana principal
root = tk.Tk()
root.title("Movimientos del Caballo")

# Entradas
ttk.Label(root, text="Número de movimientos:").grid(row=0, column=0, padx=5, pady=5)
entry_moves = ttk.Entry(root)
entry_moves.grid(row=0, column=1, padx=5, pady=5)
entry_moves.insert(0, "2")

# Botón para calcular
button_calculate = ttk.Button(root, text="Mostrar movimientos", command=show_knight_moves_result)
button_calculate.grid(row=1, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar la imagen
label_image = ttk.Label(root)
label_image.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()

