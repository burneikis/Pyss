from pyss_evaluation import evaluate
from pyss_quiescence import quiescence
import chess.polyglot

transposition_table = {}

def minimax(board, depth, alpha, beta):
    hash = chess.polyglot.zobrist_hash(board)

    if hash in transposition_table:
        transposition = transposition_table[hash]
        if transposition[1] >= depth:
            return transposition[0]

    if board.is_game_over():
        return evaluate(board)

    if depth == 0:
        return quiescence(board, alpha, beta)

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

        transposition_table[hash] = (max_eval, depth)

        return max_eval
    
    min_eval = 9999
    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, alpha, beta)
        board.pop()
        min_eval = min(min_eval, eval)
        beta = min(beta, eval)
        if beta <= alpha:
            break
    transposition_table[hash] = (min_eval, depth)
    return min_eval