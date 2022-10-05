import random
import chess

global transposition_table

transposition_table = {}

zobrist_table = [[random.randint(0, 2**64) for i in range(64)] for j in range(12)]

def zobrist_hash(board):
     hash = 0
     for square in range(64):
         piece = board.piece_at(square)
         pieceType = board.piece_type_at(square)
         if pieceType:
            hash ^= zobrist_table[pieceType + (-1 if piece.color == chess.WHITE else 5)][square]
     return hash

def add_transposition(board, score, depth):
    transposition_table[zobrist_hash(board)] = [score, depth]

def get_transposition(board):
    return transposition_table[zobrist_hash(board)]