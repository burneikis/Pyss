"""evaluates the board heuristically"""

import chess

# Piece values
# Starting with a zero because chess.PieceType is 1-indexed
values = [ 0, 100, 320, 330, 500, 900, 20000 ]

# Center squares in index form [E4, D4, E5, D5] is [28, 27, 35, 36]
center_squares = [
    27, 28,
    35, 36
]

def evaluate(board):
    """evaluates the board heuristically"""

    # Checkmate/stalemate
    if board.is_checkmate():
        return -9999 if board.turn else 9999

    if board.is_stalemate():
        return 0

    # Material
    material = 0
    for piece in board.piece_map().values():
        value = values[piece.piece_type]
        material += value if piece.color else -value

    # Mobility
    mobility = 0
    legal_moves = len(list(board.legal_moves))
    mobility += legal_moves if board.turn else -legal_moves
    # push an empty move to see the opponent's mobility
    board.push(chess.Move.null())
    legal_moves = len(list(board.legal_moves))
    mobility += legal_moves if board.turn else -legal_moves
    board.pop()

    # Center control
    center_control = 0
    for square in center_squares:
        if board.piece_at(square):
            center_control += 10 if board.piece_at(square).color else -10

    return material + center_control + mobility

# I did not include piece value tables because they are an example of human bias.
# The AI should not have to play how we tell it to.
# Center Control is biased as well, but I use it anyway.
# This is because it is fair to assume that center control is important in chess.
