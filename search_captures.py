from evaluate import evaluate

def search_captures(board, alpha, beta):
    captures = []
    for move in board.legal_moves:
        if board.is_capture(move):
            captures.append(move)
    if board.is_game_over() or len(captures) == 0:
        return evaluate(board)
    if board.turn:
        maxEval = -9999
        for move in captures:
            board.push(move)
            score = search_captures(board, alpha, beta)
            board.pop()
            maxEval = max(maxEval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = 9999
        for move in captures:
            board.push(move)
            score = search_captures(board, alpha, beta)
            board.pop()
            minEval = min(minEval, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return minEval