import sqlite3
import gradio as gr
from hanoi.hanoi import hanoi
from caballos.caballos import knight_moves_count
from reinas.reinas import solve_n_queens

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

def hanoi_interface(n, source, target, auxiliary):
    return hanoi(n, source, target, auxiliary)

def knight_moves_interface(moves):
    return knight_moves_count(moves)

def n_queens_interface(n):
    return solve_n_queens(n)

with gr.Blocks() as demo:
    gr.Markdown("# Problemas de Hanoi, Caballos y N-Reinas")
    
    with gr.Tab("Hanoi"):
        n_hanoi = gr.Number(label="Número de discos", value=3)
        source = gr.Textbox(label="Torre de origen", value="A")
        target = gr.Textbox(label="Torre de destino", value="C")
        auxiliary = gr.Textbox(label="Torre auxiliar", value="B")
        hanoi_output = gr.Textbox(label="Movimientos")
        hanoi_button = gr.Button("Resolver Hanoi")
        hanoi_button.click(hanoi_interface, inputs=[n_hanoi, source, target, auxiliary], outputs=hanoi_output)
    
    with gr.Tab("Caballos"):
        moves = gr.Number(label="Número de movimientos", value=2)
        knight_output = gr.Textbox(label="Movimientos válidos")
        knight_button = gr.Button("Calcular movimientos del caballo")
        knight_button.click(knight_moves_interface, inputs=[moves], outputs=knight_output)
    
    with gr.Tab("N-Reinas"):
        n_queens = gr.Number(label="Número de reinas", value=4)
        queens_output = gr.Textbox(label="Soluciones")
        queens_button = gr.Button("Resolver N-Reinas")
        queens_button.click(n_queens_interface, inputs=[n_queens], outputs=queens_output)

demo.launch()
