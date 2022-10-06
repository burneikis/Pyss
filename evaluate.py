import chess

values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

center_squares = [
    chess.D5, chess.E5,
    chess.D4, chess.E4
]

pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]

knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

rookstable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0
]

queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
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
        # get piece value
        value = values[piece.piece_type]
        material += value if piece.color else -value

    # Mobility
    mobility = 0
    mobility += len(list(board.legal_moves))
    board.push(chess.Move.null())
    mobility -= len(list(board.legal_moves))
    board.pop()

    # Center control
    center_control = 0
    for square in center_squares:
        if board.piece_at(square):
            center_control += 10 if board.piece_at(square).color else -10

    # Table Value
    # this is very slow
    table_value = 0
    # for piece in board.piece_map():
    #     white = board.piece_at(piece).color
    #     if board.piece_at(piece).piece_type == chess.PAWN:
    #         table_value += pawntable[piece] if white else -pawntable[chess.square_mirror(piece)]
    #     elif board.piece_at(piece).piece_type == chess.KNIGHT:
    #         table_value += knightstable[piece] if white else -knightstable[chess.square_mirror(piece)]
    #     elif board.piece_at(piece).piece_type == chess.BISHOP:
    #         table_value += bishopstable[piece] if white else -bishopstable[chess.square_mirror(piece)]
    #     elif board.piece_at(piece).piece_type == chess.ROOK:
    #         table_value += rookstable[piece] if white else -rookstable[chess.square_mirror(piece)]
    #     elif board.piece_at(piece).piece_type == chess.QUEEN:
    #         table_value += queenstable[piece] if white else -queenstable[chess.square_mirror(piece)]
    #     elif board.piece_at(piece).piece_type == chess.KING:
    #         table_value += kingstable[piece] if white else -kingstable[chess.square_mirror(piece)]


    return material + mobility + center_control + table_value 
