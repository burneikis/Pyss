from pyss_move import get_move
import chess
import chess.pgn

def get_player_move(board):
    while True:
        move = input("Enter move: ")
        try:
            move = board.parse_san(move)
            return move
        except:
            print("Invalid move")

def game(depth, white, black):
    board = chess.Board()

    board.set_board_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    pgn = chess.pgn.Game.from_board(board)
    node = pgn

    while not board.is_game_over():
        print(board)
        print("White to move" if board.turn else "Black to move")

        if board.turn and white:
            move = get_player_move(board)
        elif not board.turn and black:
            move = get_move(board, depth)
        else:
            move = get_move(board, depth)

        board.push(move)

        node = node.add_variation(move)

        print(str(pgn).split()[-2])

    print(board)
    pgn.headers["White"] = "Computer"
    pgn.headers["Black"] = "Computer"
    pgn.headers["Result"] = board.result()
    print(pgn)