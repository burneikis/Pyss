"""choose a move to play"""

import time
# multiprocess is faster than multiprocessing (idk why, im probably doing something wrong)
import multiprocess as mp # pylint: disable=import-error
from pyss_minimax import minimax

def process_function(board, move, depth, queue):
    """function to be run in multiple processes simultaneously"""
    board.push(move)
    score = minimax(board, depth - 1, float("-inf"), float("inf"))
    queue.put((move, score))

def get_move(board, depth, max_time):
    """get the highest scoring move by running an evaluation on all legal moves"""

    # start timer
    start_time = time.time()

    # set default worst moves
    best_move = None
    best_score = float("-inf")

    # create an array and queue for processes
    processes = []
    queue = mp.Queue() # pylint: disable=no-member

    # iterate through all legal moves
    for move in board.legal_moves:

        # copy the board
        board_copy = board.copy()

        # create a process for each move
        process = mp.Process(target=process_function, args=(board_copy, move, depth, queue)) # pylint: disable=not-callable
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    for process in processes:
        # if the time limit has been reached, kill all processes
        if time.time() - start_time > max_time:
            for process in processes:
                process.terminate()
            print("Max Time Reached")
            break
        process.join()

    # get the best move from the queue
    # the queue empty out as we .get move/score pairs
    while not queue.empty():
        move, score = queue.get()

        # ensure that we get the best move as black as well
        if not board.turn:
            score *= -1

        if score > best_score:
            best_move = move
            best_score = score

        # if the score is equal, I prefer to always play the same move deterministically
        # this is helpful for debugging
        elif score == best_score and str(move) < str(best_move):
            best_move = move

    return best_move
