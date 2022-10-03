from get_move import best_move
from evaluate import evaluate
from transposition import transpositions
import chess
import chess.pgn

def get_player_move(board):
    while True:
        move = input('Enter move: ')
        try:
            move = board.parse_san(move)
            if move in board.legal_moves:
                return move
        except:
            pass

def game(depth):
    board = chess.Board()

    game = chess.pgn.Game()
    game.headers["White"] = "White"
    game.headers["Black"] = "Black"
    node = game

    while not board.is_game_over():
        transpositions.clear()

        print(board)
        position = evaluate(board)
        if board.turn:
            print(f'White to move, Eval: {position/100}')
        else:
            print(f'Black to move, Eval: {position/100}')

        # Player plays white
        # if board.turn:
        #     move = get_player_move(board)
        # else:
        #     move = best_move(board, depth)

        move = best_move(board, depth)
        
        print(str(move))
        board.push(move)
        node = node.add_variation(move)

    game.headers["Result"] = board.result()

    print(board)
    print(game)

game(4)
