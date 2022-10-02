from get_move import best_move
from evaluate import evaluate
import chess
import chess.pgn

def game(depth):
    board = chess.Board()
    game = chess.pgn.Game()
    node = game
    while not board.is_game_over():
        print(board)
        position = evaluate(board)
        if board.turn:
            print(f'White to move, Eval: {position/100}')
        else:
            print(f'Black to move, Eval: {position/100}')

        move = best_move(board, depth)
        print(str(move))
        board.push(move)

        node = node.add_variation(move)

    print(board)
    print(game)
    print(f'Game over, {board.result()}')

game(2)
