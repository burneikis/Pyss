import chess

values = [ 0, 100, 320, 330, 500, 900, 20000 ]

center_squares = [
    27, 28,
    35, 36
]

def evaluate(board):
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
