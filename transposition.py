import random

global transpositions

transpositions = {}

zobrist_table = [
    [random.randint(0, 2**64) for _ in range(64)] for _ in range(12)
]

def zobrist_hash(board):
    hash = 0
    for square in range(64):
        piece = board.piece_type_at(square)
        if piece:
            hash ^= zobrist_table[piece - 1][square]
    return hash

def add_transposition(board, score):
    transpositions[zobrist_hash(board)] = score

def get_transposition(board):
    return transpositions[zobrist_hash(board)]
