import chess

def evaluate(board):
    # Checkmate/stalemate
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999

    if board.is_stalemate():
        return 0

    # Material
    material = 0
    for piece in board.piece_map().values():
        #get piece value
        if piece.piece_type == chess.PAWN:
            value = 100
        elif piece.piece_type == chess.KNIGHT:
            value = 320
        elif piece.piece_type == chess.BISHOP:
            value = 330
        elif piece.piece_type == chess.ROOK:
            value = 500
        elif piece.piece_type == chess.QUEEN:
            value = 900
        elif piece.piece_type == chess.KING:
            value = 20000

        #get piece color
        if piece.color == chess.WHITE:
            material += value
        else:
            material -= value

    # Mobility
    mobility = 0
    mobility += len(list(board.legal_moves))
    board.push(chess.Move.null())
    mobility -= len(list(board.legal_moves))
    board.pop()

    # Center control
    center_control = 0
    center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    for square in center_squares:
        if board.piece_at(square):
            if board.piece_at(square).color == chess.WHITE:
                center_control += 10
            else:
                center_control -= 10


    return material + mobility + center_control