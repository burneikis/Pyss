# Pyss - (Py(thon Che)ss)
A Simple AI for chess written in python.

## What this code does exactly
The code runs (and times itself) a chess game retrieving moves for both white and black from pyss given one argument indicating depth
The code can be modified to allow a human to input moves as well
It prints: the board, the last move, and the current turn

## How does it work?
This code basically runs using the minimax algorithm and features [alpha beta pruning](https://www.chessprogramming.org/Alpha-Beta)

More specifically this is essentially the structure
get_move:
  // returns a move
  
  // it tests every legal move from the root node simultaneously and returns the one with the best score
  
// to score a move I use minimax
minimax:
  // returns a score for a move based on the depth
  
  // this algorithm uses recursion to search deeper by a power of the number of legal moves and once reaching its limit  it evaluates the posiiton (it actually starts another search a little deeper after)
  
evaluate:
  // returns a heuristic score based purely on the current position
  
  // this is a sum of the material the number of legal moves and the center control of white
  
  // this returns a value negative if black is winning and positive if white is winning
  
 quiescence:
  // it is necessary to search deeper at the end of the minimax search because otherwise a move like QxP could be seen as good as it wins a pawn but if we stop there we might miss PxQ which would be bad
  
  // the quiescence search looks at all the potential captures and then the next layer of subsequent captures until there are no captures left to ensure that an evaluation is safe
