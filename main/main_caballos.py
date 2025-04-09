import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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
