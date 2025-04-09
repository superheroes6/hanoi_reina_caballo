import tkinter as tk
from tkinter import ttk

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        return [(origen, destino)]
    movimientos = hanoi(n - 1, origen, auxiliar, destino)
    movimientos.append((origen, destino))
    movimientos.extend(hanoi(n - 1, auxiliar, destino, origen))
    return movimientos

def mostrar_resultado_hanoi():
    n = int(entrada_discos.get())
    origen = entrada_origen.get()
    destino = entrada_destino.get()
    auxiliar = entrada_auxiliar.get()
    resultado = hanoi(n, origen, destino, auxiliar)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, "\n".join([f"{movimiento[0]} -> {movimiento[1]}" for movimiento in resultado]))

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Resolver Hanoi")

# Entradas
ttk.Label(raiz, text="Número de discos:").grid(row=0, column=0, padx=5, pady=5)
entrada_discos = ttk.Entry(raiz)
entrada_discos.grid(row=0, column=1, padx=5, pady=5)
entrada_discos.insert(0, "3")

ttk.Label(raiz, text="Torre de origen:").grid(row=1, column=0, padx=5, pady=5)
entrada_origen = ttk.Entry(raiz)
entrada_origen.grid(row=1, column=1, padx=5, pady=5)
entrada_origen.insert(0, "A")

ttk.Label(raiz, text="Torre de destino:").grid(row=2, column=0, padx=5, pady=5)
entrada_destino = ttk.Entry(raiz)
entrada_destino.grid(row=2, column=1, padx=5, pady=5)
entrada_destino.insert(0, "C")

ttk.Label(raiz, text="Torre auxiliar:").grid(row=3, column=0, padx=5, pady=5)
entrada_auxiliar = ttk.Entry(raiz)
entrada_auxiliar.grid(row=3, column=1, padx=5, pady=5)
entrada_auxiliar.insert(0, "B")

# Botón para calcular
boton_calcular = ttk.Button(raiz, text="Resolver", command=mostrar_resultado_hanoi)
boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Área de texto para mostrar el resultado
texto_resultado = tk.Text(raiz, height=15, width=40)
texto_resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
raiz.mainloop()

