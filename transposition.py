transpositions = {}

def clear_transpositions():
    transpositions.clear()

def add_transposition(board, score):
    transpositions[board] = score

def get_transposition(board):
    return transpositions.get(board)