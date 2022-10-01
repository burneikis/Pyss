from minimax import minimax

def best_move(board, depth):
    bestMove = None
    bestScore = -9999
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, -9999, 9999, False)
        board.pop()

        if not board.turn:
            score *= -1

        if score > bestScore:
            if not board.turn:
                score *= -1

            bestScore = score
            bestMove = move
    return bestMove