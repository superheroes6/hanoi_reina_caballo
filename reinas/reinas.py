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

def solve_n_queens(n):

    def is_safe(board, row, col):
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve(col, board, solutions):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                solve(col + 1, board, solutions)

    solutions = []
    solve(0, [-1] * n, solutions)
    return solutions

def n_queens_interface(n):
    return solve_n_queens(n)

with gr.Blocks() as demo:
    gr.Markdown("# Resolver N-Reinas")
    n = gr.Number(label="Número de reinas", value=4)
    output = gr.Textbox(label="Soluciones")
    button = gr.Button("Resolver")
    button.click(n_queens_interface, inputs=[n], outputs=output)

# demo.launch()  # Descomentar si se desea ejecutar directamente desde este archivo.