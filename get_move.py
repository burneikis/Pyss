from minimax import minimax

def best_move(board, depth):
    best_move = None
    best_score = -9999
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, -9999, 9999, board.turn)
        board.pop()

        if not board.turn:
            score *= -1

        if score >= best_score:
            best_score = score
            best_move = move
    return best_move