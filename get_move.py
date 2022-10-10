from minimax import minimax
from parallel_search import parallel_search
import multiprocess as mp

def process_function(board, pdepth, mdepth, q, move):
    score = parallel_search(board, pdepth, mdepth)
    q.put((move, score))

def get_move(board, depth, parallel_depth):
    best_move = None
    best_score = float("-inf")

    processes = []
    q = mp.Queue()

    for move in board.legal_moves:
        board_copy = board.copy()
        board_copy.push(move)

        p = mp.Process(target=process_function, args=(board_copy, parallel_depth, depth, q, move))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    while not q.empty():
        move, score = q.get()

        if not board.turn:
            score *= -1

        if score > best_score:
            best_move = move
            best_score = score

        elif score == best_score and str(move) < str(best_move):
            best_move = move

    return best_move