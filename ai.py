import copy
from core import *
from game import *

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

def aiMove(mainGame : Game, mainGameState : GameState) -> bool:
    #i. iterate over the board
    for i in range(8):
        for j in range(8):
            # if the colour of the piece being iterated is not the ai's (i.e. is the human's colour - opposite of the ai's, or UNDEF - the EmptySquare's colour), then continue
            if mainGame.state.gameBoard.board[i][j].colour != mainGame.whichTurn:
                continue
            # else the piece belongs to the ai
            else:
                # match case is the same as switch case (just in python). Check each piece type on each iteration. W
                match mainGame.state.gameBoard.board[i][j]:
                    case PawnPiece():
                        print("It is a Pawn")
                        gameStateCopy = copy.deepcopy(mainGameState) # use the deep copy of the current gameState to conduct legal move validations without actually modifying the mainGameState
                        # TODO: conduct legal move validation in the deepcopy(mainGameState) and do move scoring

                    case KingPiece():
                        print("It is a King")

                    case QueenPiece():
                        print("It is a Queen")

                    case RookPiece():
                        print("It is a Rook")

                    case KnightPiece():
                        print("It is a Knight")

                    case BishopPiece():
                        print("It is a Bishop")

                    case _:
                        print("error - this should never happen")
                        return False
        else:
            # TODO: after for loop has completed iterations, build a list of the 0th element from each pieces sorted list of legal move scores
            return True
