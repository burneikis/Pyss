from pyss_move import get_move
import chess
import chess.pgn
import timeit

def get_player_move(board):
    while True:
        move = input("Enter move: ")
        try:
            move = board.parse_san(move)
            return move
        except:
            print("Invalid move")

def game(depth):
    board = chess.Board()

    board.set_board_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    pgn = chess.pgn.Game.from_board(board)
    node = pgn

    while not board.is_game_over():
        print(board)
        print("White to move" if board.turn else "Black to move")

        move = get_move(board, depth) #if not board.turn else get_player_move(board)
        board.push(move) # type: ignore

        node = node.add_variation(move) # type: ignore

        print(str(pgn).split()[-2])

    print(board)
    pgn.headers["White"] = "Computer"
    pgn.headers["Black"] = "Computer"
    pgn.headers["Result"] = board.result()
    print(pgn)

if __name__ == '__main__':
    print(timeit.timeit("game(4)", setup="from __main__ import game", number=1))
