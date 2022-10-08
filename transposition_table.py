from chess.polyglot import zobrist_hash

global transposition_table

transposition_table = {}

def add_transposition(board, score, depth):
    transposition_table[zobrist_hash(board)] = [score, depth]

def get_transposition(board):
    return transposition_table[zobrist_hash(board)]