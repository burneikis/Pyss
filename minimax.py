from evaluate import evaluate
from transposition_table import add_transposition, get_transposition

def minimax(board, depth, alpha, beta):
    try:
        transposition = get_transposition(board)
        if transposition[1] >= depth:
            return transposition[0]
    except:
        pass

    if depth == 0 or board.is_game_over():
        eval = evaluate(board)
        add_transposition(board, eval, depth)
        return eval

    if board.turn:
        max_eval = -9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = 9999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval