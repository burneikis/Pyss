from evaluate import evaluate

def search_captures(board, alpha, beta):
    evaluation = evaluate(board)
    if evaluation >= beta:
        return beta
    alpha = max(alpha, evaluation)

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            evaluation = search_captures(board, alpha, beta)
            board.pop()

            if evaluation >= beta:
                return beta
            alpha = max(alpha, evaluation)

    return alpha
