from abc import ABC
from chessboard import ChessBoard
from pieces import *


class GameBoardFactory(ABC): # factory for providing new game instances. this is an abstract class. it is not real. there is no self to reference, because it will never be initialized.
    def getEmptyBoard() -> ChessBoard:
        board = ChessBoard()
        return board

    def getStandardBoard() -> ChessBoard:
        factoryBoard = ChessBoard()

        factoryBoard.board[0][0] = RookPiece        (Colour.BLACK, Position().setByXY(0,0))
        factoryBoard.board[1][0] = KnightPiece      (Colour.BLACK, Position().setByXY(1,0))
        factoryBoard.board[2][0] = BishopPiece      (Colour.BLACK, Position().setByXY(2,0))
        factoryBoard.board[3][0] = QueenPiece       (Colour.BLACK, Position().setByXY(3,0))
        factoryBoard.board[4][0] = KingPiece        (Colour.BLACK, Position().setByXY(4,0))
        factoryBoard.board[5][0] = BishopPiece      (Colour.BLACK, Position().setByXY(5,0))
        factoryBoard.board[6][0] = KnightPiece      (Colour.BLACK, Position().setByXY(6,0))
        factoryBoard.board[7][0] = RookPiece        (Colour.BLACK, Position().setByXY(7,0))
        
        # assign each pawn to it's initial position on the board
        for i in range(8):
            factoryBoard.board[i][1] = PawnPiece    (Colour.BLACK, Position().setByXY(i,1))
            factoryBoard.board[i][6] = PawnPiece    (Colour.WHITE, Position().setByXY(i,6))

        # assign each black piece to it's initial position on the board
        factoryBoard.board[0][7] = RookPiece        (Colour.WHITE, Position().setByXY(0,7))
        factoryBoard.board[1][7] = KnightPiece      (Colour.WHITE, Position().setByXY(1,7))
        factoryBoard.board[2][7] = BishopPiece      (Colour.WHITE, Position().setByXY(2,7))
        factoryBoard.board[3][7] = QueenPiece       (Colour.WHITE, Position().setByXY(3,7))
        factoryBoard.board[4][7] = KingPiece        (Colour.WHITE, Position().setByXY(4,7))
        factoryBoard.board[5][7] = BishopPiece      (Colour.WHITE, Position().setByXY(5,7))
        factoryBoard.board[6][7] = KnightPiece      (Colour.WHITE, Position().setByXY(6,7))
        factoryBoard.board[7][7] = RookPiece        (Colour.WHITE, Position().setByXY(7,7))

        return factoryBoard