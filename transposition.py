import random
import chess

global transpositions

transpositions = {}

zobrist_table = [
    [random.randint(0, 2**64) for _ in range(64)] for _ in range(12)
]

def zobrist_hash(board):
    hash = 0
    for square in range(64):
        piece = board.piece_at(square)
        pieceType = board.piece_type_at(square)
        if pieceType:
            if piece.color == chess.WHITE:
                hash ^= zobrist_table[pieceType - 1][square]
            else:
                hash ^= zobrist_table[pieceType + 5][square]
    return hash

def add_transposition(board, score, depth):
    transpositions[zobrist_hash(board)] = [score, depth]

def get_transposition(board):
    return transpositions[zobrist_hash(board)]
