from get_move import get_move
import chess
import chess.pgn

def game(depth):
    board = chess.Board()

    game = chess.pgn.Game()
    node = game

    while not board.is_game_over():
        move = get_move(board, depth)
        board.push(move)
        node = node.add_variation(move)

    game.headers["White"] = "Computer"
    game.headers["Black"] = "Computer"
    game.headers["Result"] = board.result()
    print(game)

if __name__ == '__main__':
    game(2)
