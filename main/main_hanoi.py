import tkinter as tk
from tkinter import ttk
from hanoi.hanoi import hanoi

def show_hanoi_result():
    n = int(entry_disks.get())
    source = entry_source.get()
    target = entry_target.get()
    auxiliary = entry_auxiliary.get()
    result = hanoi(n, source, target, auxiliary)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n".join([f"{move[0]} -> {move[1]}" for move in result]))

# Crear la ventana principal
root = tk.Tk()
root.title("Resolver Hanoi")

# Entradas
ttk.Label(root, text="Número de discos:").grid(row=0, column=0, padx=5, pady=5)
entry_disks = ttk.Entry(root)
entry_disks.grid(row=0, column=1, padx=5, pady=5)
entry_disks.insert(0, "3")

ttk.Label(root, text="Torre de origen:").grid(row=1, column=0, padx=5, pady=5)
entry_source = ttk.Entry(root)
entry_source.grid(row=1, column=1, padx=5, pady=5)
entry_source.insert(0, "A")

ttk.Label(root, text="Torre de destino:").grid(row=2, column=0, padx=5, pady=5)
entry_target = ttk.Entry(root)
entry_target.grid(row=2, column=1, padx=5, pady=5)
entry_target.insert(0, "C")

ttk.Label(root, text="Torre auxiliar:").grid(row=3, column=0, padx=5, pady=5)
entry_auxiliary = ttk.Entry(root)
entry_auxiliary.grid(row=3, column=1, padx=5, pady=5)
entry_auxiliary.insert(0, "B")

# Botón para calcular
button_calculate = ttk.Button(root, text="Resolver", command=show_hanoi_result)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Área de texto para mostrar el resultado
result_text = tk.Text(root, height=15, width=40)
result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()
