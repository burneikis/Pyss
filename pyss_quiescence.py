from pyss_evaluation import evaluate

def quiescence(board, alpha, beta): 
    captures = [i for i in board.legal_moves if board.is_capture(i)]

    stand_pat = evaluate(board)

    if board.turn:
        if stand_pat >= beta:
            return beta
        if alpha < stand_pat:
            alpha = stand_pat

        for move in captures:
            board.push(move)
            score = quiescence(board, alpha, beta)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score

        return alpha

    if stand_pat <= alpha:
        return alpha
    if beta > stand_pat:
        beta = stand_pat
    for move in captures:
        board.push(move)
        score = quiescence(board, alpha, beta)
        board.pop()
        if score <= alpha:
            return alpha
        if score < beta:
            beta = score
    return beta
