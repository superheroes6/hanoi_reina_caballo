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