"""chess game"""

import chess
import chess.pgn
from pyss_move import get_move

def get_player_move(board):
    """gets a move from the player"""
    while True:
        move = input("Enter move: ")
        try:
            move = board.parse_san(move)
            return move
        except ValueError:
            print("Invalid move")

def game(depth, white, black, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", turn = True):
    """
    main game loop
    depth is the depth of the search tree
    white and black are booleans that determine if the player is white or black
    fen is the position (default is the starting position)
    turn is a boolean that determines if it is white's turn at start (default is True)
    """

    # create a new board
    board = chess.Board()

    # setup the board
    board.set_board_fen(fen)

    # set the turn
    board.turn = turn

    # start a new pgn from the current board
    # (specifically .from_board so that the pgn will start from the current position)
    pgn = chess.pgn.Game.from_board(board)
    node = pgn

    # loop until the game is over
    while not board.is_game_over():

        # print the board and turn
        print(board)
        print("White to move" if board.turn else "Black to move")

        # get a move from the player or the computer
        if board.turn and white:
            move = get_player_move(board)
        elif not board.turn and black:
            move = get_player_move(board)
        else:
            move = get_move(board, depth)

        # make the move
        board.push(move)

        # add the move to the pgn as a 'variation'
        node = node.add_variation(move)

        # print the last move from the pgn (the move we just made)
        print(str(pgn).split()[-2])

    # when the game is over, print the board and the entire pgn
    print(board)
    pgn.headers["White"] = "Player" if white else "Computer"
    pgn.headers["Black"] = "Player" if black else "Computer"
    pgn.headers["Result"] = board.result()
    print(pgn)
