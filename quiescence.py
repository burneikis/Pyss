from evaluate import evaluate

def quiescence(board, alpha, beta, max_player): 
    captures = [i for i in board.legal_moves if board.is_capture(i)]

    stand_pat = evaluate(board)

    if max_player:
        if stand_pat >= beta:
            return beta
        if alpha < stand_pat:
            alpha = stand_pat

        for move in captures:
            board.push(move)
            score = quiescence(board, alpha, beta, False)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score

        return alpha

    else:
        if stand_pat <= alpha:
            return alpha
        if beta > stand_pat:
            beta = stand_pat

        for move in captures:
            board.push(move)
            score = quiescence(board, alpha, beta, True)
            board.pop()

            if score <= alpha:
                return alpha
            if score < beta:
                beta = score

        return beta