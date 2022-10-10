from concurrent.futures import process
from evaluate import evaluate
from minimax import minimax

import multiprocess as mp

def parallel_function(board, depth, q, mdepth):
    score = parallel_search(board, depth, mdepth)
    q.put(score)

def parallel_search(board, pdepth, mdepth):
    '''
    score all moves and return the lowest or highest score
    '''
    if board.is_game_over():
        return evaluate(board)

    if pdepth == 0:
        return minimax(board, mdepth, float("-inf"), float("inf"))

    #if pdepth isnt 0 make processes for each move
    processes = []
    q = mp.Queue()

    if board.turn:
        best_score = float("-inf")
        for move in board.legal_moves:
            board_copy = board.copy()
            board_copy.push(move)
            
            p = mp.Process(target=parallel_function, args=(board_copy, pdepth - 1, q, mdepth))
            processes.append(p)

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        while not q.empty():
            score = q.get()
            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")
        for move in board.legal_moves:
            board_copy = board.copy()
            board_copy.push(move)

            p = mp.Process(target=parallel_function, args=(board_copy, pdepth - 1, q, mdepth))
            processes.append(p)

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        while not q.empty():
            score = q.get()
            best_score = min(best_score, score)

        return best_score