import re
import typing
from chessboard import ChessBoard
from factory import GameBoardFactory
from pieces import *

# Regular Expression for valid moves:
#   (letter-from-a-to-h) (number-from-1-to-8) hyphen (letter-from-a-to-h) (number-from-1-to-8)
# (the parentheses around each letter and number capture it in a capture group)
# So, if there's a match, the capture groups will be:
#   source_file = match.group(1)
#   source_rank = match.group(2)
#   dest_file = match.group(3)
#   dest_rank = match.group(4)
longNotationPattern = "^([a-h])([1-8])-([a-h])([1-8])$"




class GameState:
    gameBoard: ChessBoard = GameBoardFactory.getStandardBoard()   # gameBoard is a ChessBoard-like object

    # kingDict stores key:value pair of Colour:kingPosition, which is updated each turn. Designed to keep track of each colour's king position for reference in the isKingCheck function
    kingDict = {}
    # these two lists should store the list of pieces (for each respective colour) which are still on the board. By default, all pieces are on the board. When a piece captures another piece, new behaviour has to be written to remove them from this list.
    whitePiecesOnBoard = []
    blackPiecesOnBoard = []

    def isValidMove(self, gameBoard : ChessBoard, sourcePiece : Piece, location : Position):
        match sourcePiece:
            case EmptySquare():
                return False
            case PawnPiece():
                dx = abs(location.x - sourcePiece.location.x)

                #make sure you're not trying to validate a move that would land on one of your own pieces
                if gameBoard.board[location.x][location.y].colour == sourcePiece.colour:
                    return False
                
                if sourcePiece.location.x == location.x: 
                    if sourcePiece.colour == Colour.WHITE:
                        if location.y == sourcePiece.location.y - 1:
                            return True
                        elif sourcePiece.location.y == 6 and location.y == sourcePiece.location.y - 2:
                            return True
                        else:
                            return False
                    else:
                        if location.y == sourcePiece.location.y + 1:
                            return True
                        elif sourcePiece.location.y == 1 and location.y == sourcePiece.location.y + 2:
                            return True
                        else:
                            return False
                elif dx == 1:
                    if sourcePiece.colour == Colour.WHITE:
                        if location.y == sourcePiece.location.y - 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))) is not EmptySquare:
                            return True
                        else:
                            return False
                    else:
                        if location.y == sourcePiece.location.y + 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))): 
                            return True
                        else:
                            return False
                else:
                    return False
            case RookPiece():
                dx = abs(location.x - sourcePiece.location.x)
                dy = abs(location.y - sourcePiece.location.y)

                #make sure you're not trying to validate a move that would land on one of your own pieces
                if gameBoard.board[location.x][location.y].colour == sourcePiece.colour:
                    return False

                # Check if the move is on the cardinal
                if dx != 0 and dy != 0:
                    return False

                # Check for pieces in the east direction
                if location.x > sourcePiece.location.x:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x + i),(sourcePiece.location.y)))) is not EmptySquare:
                            return False
                # Check for pieces in the west direction
                elif location.x < sourcePiece.location.x:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x - i), (sourcePiece.location.y)))) is not EmptySquare:
                            return False
                # Check for pieces in the south direction
                elif location.y > sourcePiece.location.y:
                    for i in range(1, dy):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x), (sourcePiece.location.y + i)))) is not EmptySquare:
                            return False
                # Check for pieces in the north direction
                elif location.y < sourcePiece.location.y:
                    for i in range(1, dy):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x), (sourcePiece.location.y - i)))) is not EmptySquare:
                            return False
                return True
            case KnightPiece():
                return self
            case BishopPiece():
                dx = abs(location.x - sourcePiece.location.x)
                dy = abs(location.y - sourcePiece.location.y)

                #make sure you're not trying to validate a move that would land on one of your own pieces
                if gameBoard.board[location.x][location.y].colour == sourcePiece.colour:
                    return False
                # Check if the move is on the diagonal
                if dx != dy:
                    return False
                # Check for pieces in the northeast direction
                if location.x > sourcePiece.location.x and location.y > sourcePiece.location.y:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x + i),(sourcePiece.location.y + i)))) is not EmptySquare:
                            return False
                # Check for pieces in the northwest direction
                elif location.x < sourcePiece.location.x and location.y > sourcePiece.location.y:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x - i),(sourcePiece.location.y + i)))) is not EmptySquare:
                            return False
                # Check for pieces in the southeast direction
                elif location.x > sourcePiece.location.x and location.y < sourcePiece.location.y:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x + i),(sourcePiece.location.y - i)))) is not EmptySquare:
                            return False
                # Check for pieces in the southwest direction
                elif location.x < sourcePiece.location.x and location.y < sourcePiece.location.y:
                    for i in range(1, dx):
                        if type(gameBoard.getPieceFromBoard(Position((sourcePiece.location.x - i),(sourcePiece.location.y - i)))) is not EmptySquare:
                            return False
                return True
            
            case KingPiece():
                return self
            case QueenPiece():
                return self

    # just move the piece; valibdation is done elsewhere
    def movePiece(self, sourcePiece : Piece, destinationPosition : Position):
        moveTest = self.isValidMove(self.gameBoard, sourcePiece, destinationPosition)
        if moveTest:
            # first, take the sourcePiece off the board (by replacing it with an EmptySquare)
            self.gameBoard.board[sourcePiece.location.x][sourcePiece.location.y] = EmptySquare()
            # next, assign the location of the source piece to the destination position (this is in the in-memory representation of the source piece)
            sourcePiece.location = destinationPosition
            # finally, update the in-memory representation of the board by putting the source piece on the destination position.
            # note that this will also destroy any underlying piece on the destination square. 
            self.gameBoard.board[destinationPosition.x][destinationPosition.y] = sourcePiece
            # TODO: based on the note above, I will need to update the gamestate with the lost pieces which are captured (when they are on the destination square). 
            # I'll need to do a test on whether the destination square is occupied during this method.
            return True
        else:
            # TODO: handle cases when the move is not valid (i.e)
            print("this is not a valid move, try again. \n")
            return False


class Game:

    def __init__(self):
        self.state = GameState()
        self.whichTurn = Colour.WHITE
        self.turnCounter = 0 

    def isValidMove(self, gameBoard : ChessBoard, location : Position, sourcePiece : Piece):
            match sourcePiece:
                case EmptySquare():
                    return False
                
                case PawnPiece():
                    dx = abs(location.x - sourcePiece.location.x)
                    
                    if sourcePiece.colour == self.whichTurn: #make sure you're not trying to validate a move that would land on one of your own pieces
                        return False
                    
                    if sourcePiece.location.x == location.x: 
                        if self.colour == Colour.WHITE:
                            if location.y == sourcePiece.location.y - 1:
                                return True
                            elif sourcePiece.location.y == 6 and location.y == sourcePiece.location.y - 2:
                                return True
                            else:
                                return False
                        else:
                            if location.y == sourcePiece.location.y + 1:
                                return True
                            elif sourcePiece.location.y == 1 and location.y == sourcePiece.location.y + 2:
                                return True
                            else:
                                return False
                    elif dx == 1:
                        if self.colour == Colour.WHITE:
                            if location.y == sourcePiece.location.y - 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))) is not EmptySquare:
                                return True
                            else:
                                return False
                        else:
                            if location.y == sourcePiece.location.y + 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))): 
                                return True
                            else:
                                return False
                    else:
                        return False
                    return self
                case RookPiece():
                    return self
                case KnightPiece():
                    return self
                case BishopPiece():
                    return self
                case KingPiece():
                    return self
                case QueenPiece():
                    return self

    def moveToNextTurn(self):
        self.turnCounter += 1
        if self.turnCounter % 2 == 0:
            self.whichTurn = Colour.WHITE
        else:
            self.whichTurn = Colour.BLACK

    def askForMove(self, message : str) -> typing.Tuple[Position, Position]: # global utility function for checking if a piece move is valid
        # ask the user to input the X position for the piece they want to move
        print(message)
        print(f"{str(self.whichTurn)}'s score is: {self.evaluateBoard()}\n")
        gotValidMove = False
        while not gotValidMove:
            userInput = input("Enter your move in Long Chess Notation (eg., b1-a3): ")
            # re.search() returns re.Match object which evaluates True if userInput matches the regular expression groups in longNotationPattern
            match = re.search(longNotationPattern, userInput)
            if not match:
                print("Incorrect syntax -- try again")
                continue

            # stores the match.group(1) and match.group(2) from the user's input as a Position object instance. These groups represent the rank and file of the source destination in the form of long algebraic notation.
            sourceLocation = Position().setByFileRank(match.group(1), match.group(2))
            # similary to sourceLocation's comment, destLocation stores the matching group(3) and group(4) from the user's input as a Position object instance.
            destLocation = Position().setByFileRank(match.group(3), match.group(4))

            # userSelection stores the return value for the getPieceFromBoard() method from the ChessBoard Class. 
            # The .getPieceFromBoard() method takes a Position as it's only argument, and returns the piece contained by the (x, y) board position: (_x property, _y property) of the Position argument
            userPieceSelection = self.state.gameBoard.getPieceFromBoard(sourceLocation)
            
            # check if the piece the user wants to move is their colour
            if userPieceSelection.colour == self.whichTurn:
                self.state.gameBoard
                # return the Positions of the user's sourceLocation and destLocation
                return (sourceLocation, destLocation)

            # check if the user is trying to select an EmptySquare Piece
            if userPieceSelection == EmptySquare:
                print("Source square does not contain a piece - try again")

            # if all conditions are not valid, it means the user is trying to move a Piece which isn't their own. repeat the loop.
            print(f"{str(userPieceSelection)} - Wrong colour - try again ")

    def doTurn(self):
        # move stores the tuple (sourceLocation : Position, DestLocation : Position) representing the user's desired move
        move = self.askForMove(f"It's {str(self.whichTurn)}'s turn")
        # movePiece(sourcePiece : Piece, destinationPosition : typing.Tuple(Position, Position))
        if not self.state.movePiece(self.state.gameBoard.getPieceFromBoard(move[0]), move[1]):
            self.doTurn()

    def evaluateBoard(self): # basic evaluation function which iterates over the board and calculates the given player's score
        whiteScore = 0
        blackScore = 0

        for i in range(8):
            for j in range(8):
                if self.whichTurn == Colour.WHITE:
                    piece = self.state.gameBoard.board[i][j]
                    if str(piece) == 'WP':
                        whiteScore += 1
                    elif str(piece)  == 'WN' or str(piece) == 'WB':
                        whiteScore += 3
                    elif str(piece)  == 'WR':
                        whiteScore += 5
                    elif str(piece)  == 'WQ':
                        whiteScore += 9
                    elif str(piece)  == 'BP':
                        whiteScore -= 1
                    elif str(piece)  == 'BN' or str(piece) == 'BB':
                        whiteScore -= 3
                    elif str(piece)  == 'BR':
                        whiteScore -= 5
                    elif str(piece)  == 'BQ':
                        whiteScore -= 9
                    elif str(piece) == "''":
                        whiteScore += 0
                    else:
                        return whiteScore
                else:
                    piece = self.state.gameBoard.board[i][j]
                    if str(piece) == 'WP':
                        blackScore -= 1
                    elif str(piece) == 'WN' or str(piece) == 'WB':
                        blackScore -= 3
                    elif str(piece) == 'WR':
                        blackScore -= 5
                    elif str(piece) == 'WQ':
                        blackScore -= 9
                    elif str(piece) == 'BP':
                        blackScore += 1
                    elif str(piece) == 'BN' or str(piece) == 'BB':
                        blackScore += 3
                    elif str(piece) == 'BR':
                        blackScore += 5
                    elif str(piece) == 'BQ':
                        blackScore += 9
                    elif str(piece) == "''":
                        blackScore += 0
                    else:
                        return blackScore

    # global utility function that can be called whenever you need to check if a King is in check. 
    def isKingCheck(self, colour : Colour): 
        # Get the colour's king Position
        for i in range(8):
            for j in range(8):
                if type(self.state.gameBoard.board[i][j]) is KingPiece and colour == self.state.gameBoard.board[i][j].colour:
                    correctKingPos = self.state.gameBoard.board[i][j].location

        # Iterate over the current board, and for each Piece use the isValidMove method (passing the King's position in as the destinationLocation for the method). 
        for i in range(8):
            for j in range(8):
                # If the piece being evaluated puts the king in check, then isKingCheck returns True
                if type(self.state.gameBoard.board[i][j]) is not EmptySquare and self.state.gameBoard.board[i][j].isValidMove(self.state.gameBoard, correctKingPos) == True:
                    return True
        return False

    def gameLoop(self):
        print("\n")
        print("-----------")
        print("Here is the game board: \n")
        print(self.state.gameBoard)
        self.doTurn()
        self.moveToNextTurn()