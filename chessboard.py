from core import Position
from pieces import EmptySquare, Piece


class ChessBoard:
    # define the initial board as a 2D array, where '' represents an empty square
    board = [[EmptySquare() for j in range(8)] for i in range(8)]

    def getPieceFromBoard(self, location : Position) -> Piece: # method to find the piece on a specified position of the board
        return self.board[location.x][location.y]

    def __str__(self):  # redefine the __str__ special function to print the chess board out with new lines after every outer list element
        ret = ""

        # i is outside list (X)
        for i in range(8):
            ret = ret + str(8-i) + " "
            # j is inside lists (Y)
            for j in range(8):
                ret = ret + str(self.board[j][i]) + " "
                if j == 7:
                    ret = ret + "\n"

        ret = ret + "  " + \
            "  ".join(["a", "b", "c", "d", "e", "f", "g", "h"]) + "\n"
        return ret
    

