from get_move import best_move
from evaluate import evaluate
import chess

board = chess.Board()

def game(depth):
    played_moves = []
    while not board.is_game_over():
        print(board)
        position = evaluate(board)
        if board.turn:
            print(f'White to move, Position: {position}')
        else:
            print(f'Black to move, Position: {position}')

        move = best_move(board, depth)
        board.push(move)

        played_moves.append(str(move))

    print(board)
    print(played_moves)
    print(f'Game over, {board.result()}')

game(2)
