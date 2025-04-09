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

def knight_moves_interface(moves):
    return knight_moves_count(moves)

with gr.Blocks() as demo:
    gr.Markdown("# Movimientos del Caballo")
    moves = gr.Number(label="Número de movimientos", value=2)
    output = gr.Textbox(label="Movimientos válidos")
    button = gr.Button("Calcular")
    button.click(knight_moves_interface, inputs=[moves], outputs=output)

# demo.launch()  # Descomentar si se desea ejecutar directamente desde este archivo.