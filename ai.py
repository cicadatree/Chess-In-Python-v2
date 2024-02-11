from __future__ import annotations
from core import *
from game import *
import re
import copy

# This file will be used to contain the code for 
# the computer player's decision-making code.

# The computer player will always be whichever 
# colour the human does not choose to play as, 
# though this has yet to be implemented (see the "menu case" in the ChessApp class in application.py)

# 1. AI makes move decisions for the opposite colour of the human player
#
# 2. AI makes move decisions using a for else loop that evaluates like this:
#
##   for (iterate over the current board):
###     i. iterating over the current board state. On each iteration, return False if the square is an EmptySquare or the opposite colour's piece (narrow in on the remaining subset of squares; only the ai colour's pieces)
###     ii. for each of the AI's own pieces in the iteration, evaluate all possible legal moves which the piece could make (run the pieces isValidMove method for the [i][j] board location which that piece is on)
###     iii. create an empty list. for each legal move of the given piece, score the move based on it's outcome (using the evaluateBoard global utility function). Add points to the given move if that move results in a capture; deduct points for moves that expose the AI's own king/queen.
###     iv. sort the list (appended with each legal move for the given piece) in descending order (from highest to lowest score)
##   else (in the final iteration, return the best of all possible moves)
###     i. take the first index from each piece's move score lists (which should be each pieces best move), add them to a new list 
###     ii. sort the new list in descending order and return the higesht-scoring move among all legal moves

class aiMove:
    def __init__( self, colour, max_depth ):
        self.colour = colour
        self.max_dept = max_depth

    def evaluate_board( self, board ):
        # TODO: implement a simple evaluation function to score the given board state
        return 0
    
    def minimax( self, board : GameState, depth, is_maximizing ):
        # Perform the minimax algorithm

        if depth == 0:
            return self.evaluate_board( board )
        
        legal_moves = board.isValidMove(self.colour)
