from minimax import minimax
import multiprocess as mp

def thread_function(board, depth, move, queue):
    board.push(move)
    score = minimax(board, depth - 1, -9999, 9999)
    board.pop()

    queue.put((move, score))

def get_move(board, depth):
    best_move = None
    best_score = -9999

    processes = []
    q = mp.Queue()

    for move in board.legal_moves:
        board_copy = board.copy()

        p = mp.Process(target=thread_function, args=(board_copy, depth, move, q))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    for move in board.legal_moves:
        move, score = q.get()

        if not board.turn:
            score *= -1
        
        if score >= best_score:
            best_score = score
            best_move = move

    return best_move