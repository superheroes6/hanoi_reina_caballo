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