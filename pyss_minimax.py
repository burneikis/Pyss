"""my implementation of a minimax algorithm with alpha-beta pruning and transposition tables"""

import chess.polyglot
from pyss_evaluation import evaluate
from pyss_quiescence import quiescence

# create an empty table
transposition_table = {}

def minimax(board, depth, alpha, beta):
    """minimax algorithm with alpha beta pruning and transposition tables"""

    # hash the current board
    board_hash = chess.polyglot.zobrist_hash(board)

    # check if the board is in the table and if the depth is >= to the depth in the table
    # if so, return the value from the table
    if board_hash in transposition_table:
        transposition = transposition_table[board_hash]
        if transposition[1] >= depth:
            return transposition[0]

    # if the game is over, return the evaluation
    # (dont need quiescence because the game is over)
    if board.is_game_over():
        return evaluate(board)

    # if the depth is 0, return the quiescence search value
    if depth == 0:
        return quiescence(board, alpha, beta)

    # if it is white's turn we want the maximum score
    if board.turn:
        # this is standard minimax
        max_eval = -9999
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta)
            board.pop()
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        # add the board to the table of calculated boards
        transposition_table[board_hash] = (max_eval, depth)

        return max_eval

    # if it is black's turn we want the minimum score
    # we will only get here if it is not white's turn because of the return statement
    min_eval = 9999
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, alpha, beta)
        board.pop()
        min_eval = min(min_eval, score)
        beta = min(beta, score)
        if beta <= alpha:
            break

    # add the board to the table of calculated boards
    transposition_table[board_hash] = (min_eval, depth)

    return min_eval

# my implementation of transposition tables only works at higher depths
