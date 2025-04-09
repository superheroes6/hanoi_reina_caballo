import sqlite3
import gradio as gr

class SQL:

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

def hanoi(n, source, target, auxiliary):

    if n == 1:
        return [(source, target)]
    moves = hanoi(n - 1, source, auxiliary, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, auxiliary, target, source))
    return moves

def hanoi_interface(n, source, target, auxiliary):
    return hanoi(n, source, target, auxiliary)

with gr.Blocks() as demo:
    gr.Markdown("# Resolver Hanoi")
    n = gr.Number(label="Número de discos", value=3)
    source = gr.Textbox(label="Torre de origen", value="A")
    target = gr.Textbox(label="Torre de destino", value="C")
    auxiliary = gr.Textbox(label="Torre auxiliar", value="B")
    output = gr.Textbox(label="Movimientos")
    button = gr.Button("Resolver")
    button.click(hanoi_interface, inputs=[n, source, target, auxiliary], outputs=output)

# demo.launch()  # Descomentar si se desea ejecutar directamente desde este archivo.