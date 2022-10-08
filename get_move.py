from minimax import minimax
import threading

def get_move(board, depth):
    best_move = None
    best_score = -9999

    def thread_function(board, depth, move):
        board.push(move)
        score = minimax(board, depth - 1, -9999, 9999)
        board.pop()

        if not board.turn:
            score *= -1

        nonlocal best_score
        nonlocal best_move

        if score >= best_score:
            best_score = score
            best_move = move

    threads = []

    for move in board.legal_moves:
        board_copy = board.copy()

        t = threading.Thread(target=thread_function, args=(board_copy, depth, move))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
         
    return best_move