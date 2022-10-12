"""quiescence search"""

# I initially had a problem with the quiescence search only working for white
# I was using pseudocode from chessprogramming.org

# So I manually wrote my own code using the pseudocode from the wiki for white,
# and the opposite for black.

from pyss_evaluation import evaluate

def quiescence(board, alpha, beta):
    """my code for quiescence searching"""
    captures = [i for i in board.legal_moves if board.is_capture(i)]

    stand_pat = evaluate(board)

    # use this for white
    # standard quiescence search
    if board.turn:
        if stand_pat >= beta:
            return beta

        alpha = max(alpha, stand_pat)

        for move in captures:
            board.push(move)
            score = quiescence(board, alpha, beta)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score

        return alpha

    # use this for black
    # does the opposite of the above
    if stand_pat <= alpha:
        return alpha

    beta = min(beta, stand_pat)

    for move in captures:
        board.push(move)
        score = quiescence(board, alpha, beta)
        board.pop()
        if score <= alpha:
            return alpha
        if score < beta:
            beta = score
    return beta
