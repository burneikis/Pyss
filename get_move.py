from minimax import minimax
from parallel_search import parallel_search

def get_move(board, depth):
    best_move = None
    best_score = float("-inf")

    for move in board.legal_moves:
        board.push(move)
        score = parallel_search(board, 1, depth - 1)
        board.pop()

        if not board.turn:
            score *= -1
        
        if score > best_score:
            best_score = score
            best_move = move

        elif score == best_score and str(move) < str(best_move):
            best_move = move

    return best_move