from minimax import minimax
import multiprocess as mp

def process_function(board, move, depth, q):
    board.push(move)
    score = minimax(board, depth, float("-inf"), float("inf"))
    q.put((move, score))

def get_move(board, depth, parallel_depth):
    best_move = None
    best_score = float("-inf")

    processes = []
    q = mp.Queue()

    for move in board.legal_moves:
        board_copy = board.copy()

        p = mp.Process(target=process_function, args=(board_copy, move, depth, q))
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