from minimax import minimax

def get_move(board, depth):
    best_move = None
    best_score = float("-inf")

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, float("-inf"), float("inf"))
        board.pop()

        if not board.turn:
            score *= -1
        
        if score > best_score:
            best_score = score
            best_move = move

        elif score == best_score and str(move) < str(best_move):
            best_move = move

    return best_move