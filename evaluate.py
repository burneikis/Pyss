import chess
#from piece_tables import piece_square_tables

values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# center_squares = [
#     chess.D5, chess.E5,
#     chess.D4, chess.E4
# ]

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
    # mobility = 0
    # mobility += len(list(board.legal_moves))
    # board.push(chess.Move.null())
    # mobility -= len(list(board.legal_moves))
    # board.pop()

    # Center control
    # center_control = 0
    # for square in center_squares:
    #     if board.piece_at(square):
    #         center_control += 10 if board.piece_at(square).color else -10

    # Table Value
    # this is very slow
    # table_value = 0
    # for piece in board.piece_map():
    #     white = board.piece_at(piece).color
    #     piece_type = board.piece_at(piece).piece_type
    #     table_value += piece_square_tables[piece_type][piece] if white else -piece_square_tables[piece_type][piece]

    return material #+ mobility + center_control + table_value 
