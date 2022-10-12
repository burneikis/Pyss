"""choose a move to play"""

# multiprocess is faster than multiprocessing (idk why, im probably doing something wrong)
import multiprocess as mp
from pyss_minimax import minimax

def process_function(board, move, depth, queue):
    """function to be run in multiple processes simultaneously"""
    board.push(move)
    score = minimax(board, depth - 1, float("-inf"), float("inf"))
    queue.put((move, score))

def get_move(board, depth):
    """get the highest scoring move by running an evaluation on all legal moves"""

    # set default worst moves
    best_move = None
    best_score = float("-inf")

    # create an array and queue for processes
    processes = []
    queue = mp.Queue()

    # iterate through all legal moves
    for move in board.legal_moves:

        # copy the board
        board_copy = board.copy()

        # create a process for each move
        process = mp.Process(target=process_function, args=(board_copy, move, depth, queue))
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    for process in processes:
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
