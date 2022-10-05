from get_move import best_move
import chess
import chess.pgn

def game(depth):
    board = chess.Board()

    game = chess.pgn.Game()
    node = game

    while not board.is_game_over():
        print(board)
        if board.turn:
            print("White to move")
        else:
            print("Black to move")

        move = best_move(board, depth)
        
        print(f'{move[0]}: {move[1]/100}')
        board.push(move[0])
        node = node.add_variation(move[0])

        game.headers["Result"] = board.result()

    print(board)
    print(game)

game(2)
