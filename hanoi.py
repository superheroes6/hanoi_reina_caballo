def hanoi(n, source, target, auxiliary):

    if n == 1:
        return [(source, target)]
    moves = hanoi(n - 1, source, auxiliary, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, auxiliary, target, source))
    return moves