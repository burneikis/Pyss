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
        if board.turn:
            print("White to move")
        else:
            print("Black to move")

        # Player plays white
        # if board.turn:
        #     move = get_player_move(board)
        # else:
        #     move = best_move(board, depth)

        move = best_move(board, depth)
        
        print(f'{move[0]}: {move[1]/100}')
        board.push(move[0])
        node = node.add_variation(move[0])

    game.headers["Result"] = board.result()

    print(board)
    print(game)

game(2)
