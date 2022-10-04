from evaluate import evaluate

def get_captures(board):
    captures = []
    for move in board.legal_moves:
        if board.is_capture(move):
            captures.append(move)
    return captures


def minimax_cap(board, alpha, beta):
    captures = get_captures(board)
    if len(captures) == 0:
        return evaluate(board)
    if board.turn:
        maxEval = -9999
        for move in captures:
            board.push(move)
            eval = minimax_cap(board, alpha, beta)
            board.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = 9999
        for move in captures:
            board.push(move)
            eval = minimax_cap(board, alpha, beta)
            board.pop()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval