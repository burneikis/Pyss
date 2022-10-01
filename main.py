from get_move import best_move
from evaluate import evaluate
import chess

board = chess.Board()

while not board.is_game_over():
    print(board)
    position = evaluate(board)
    if board.turn:
        print(f'White to move, Position: {position}')
    else:
        print(f'Black to move, Position: {position}')

    move = best_move(board, 4)
    board.push(move)

print(board)
print(f'Game over, {board.result()}')
