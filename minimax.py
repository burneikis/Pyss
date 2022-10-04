from evaluate import evaluate
from search_captures import minimax_cap
from transposition import add_transposition, get_transposition

def minimax(board, depth, alpha, beta, how_deep):
    try:
        transposition = get_transposition(board, depth)
        if transposition[1] >= how_deep:
            return transposition[0]
    except:
        pass

    if depth == 0 or board.is_game_over():
        evaluation = minimax_cap(board, alpha, beta, how_deep)
        add_transposition(board, evaluation, how_deep)
        return evaluation
    if board.turn:
        maxEval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, how_deep + 1)
            board.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = 9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, how_deep + 1)
            board.pop()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval