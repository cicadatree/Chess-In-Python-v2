from core import Colour, Position


class Piece:
    colour: Colour
    location: Position
    def __init__(self, colour : Colour, location : Position):
        self.colour = colour
        self.location = location

    def __str__(self) -> str:  # redefine the __str__ special function to print the
        return str(self.colour) + self.getPieceType()

    def getColour(self):
        return self.colour

    def getPieceType(self):
        if type(self) == PawnPiece:
            return "P"
        elif type(self) == KnightPiece:
            return "N"
        elif type(self) == RookPiece:
            return "R"
        elif type(self) == QueenPiece:
            return "Q"
        elif type(self) == KingPiece:
            return "K"
        elif type(self) == BishopPiece:
            return "B"
        else:
            return "''"

    __repr__ = __str__


class EmptySquare(Piece):
    def __init__(self):
        super().__init__(Colour.UNDEF, Position())

    # location is a placeholder required for the isKingCheck method
    def isValidMove(self, gameBoard, location : Position):
        return False


class PawnPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)

    def isValidMove(self, gameBoard, location : Position):

        dx = abs(location.x - self.location.x)

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == self.colour:
            return False
        
        if self.location.x == location.x: 
            if self.colour == Colour.WHITE:
                if location.y == self.location.y - 1:
                    return True
                elif self.location.y == 6 and location.y == self.location.y - 2:
                    return True
                else:
                    return False
            else:
                if location.y == self.location.y + 1:
                    return True
                elif self.location.y == 1 and location.y == self.location.y + 2:
                    return True
                else:
                    return False
        elif dx == 1:
            if self.colour == Colour.WHITE:
                if location.y == self.location.y - 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))) is not EmptySquare:
                    return True
                else:
                    return False
            else:
                if location.y == self.location.y + 1 and type(gameBoard.getPieceFromBoard(Position((location.x),(location.y)))): 
                    return True
                else:
                    return False
        else:
            return False


class RookPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)

    def isValidMove(self, location : Position, gameBoard):
        dx = abs(location.x - self.location.x)
        dy = abs(location.y - self.location.y)

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == self.colour:
            return False

        # Check if the move is on the cardinal
        if dx != 0 and dy != 0:
            return False

        # Check for pieces in the east direction
        if location.x > self.location.x:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y)))) is not EmptySquare:
                    return False
        # Check for pieces in the west direction
        elif location.x < self.location.x:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i), (self.location.y)))) is not EmptySquare:
                    return False
        # Check for pieces in the south direction
        elif location.y > self.location.y:
            for i in range(1, dy):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the north direction
        elif location.y < self.location.y:
            for i in range(1, dy):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y - i)))) is not EmptySquare:
                    return False
        return True


class BishopPiece(Piece):
    def __init__(self, colour, location: Position):
        super().__init__(colour, location)

    def isValidMove(self, location : Position, gameBoard):
        dx = abs(location.x - self.location.x)
        dy = abs(location.y - self.location.y)

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == self.colour:
            return False

        # Check if the move is on the diagonal
        if dx != dy:
            return False

        # Check for pieces in the northeast direction
        if location.x > self.location.x and location.y > self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the northwest direction
        elif location.x < self.location.x and location.y > self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the southeast direction
        elif location.x > self.location.x and location.y < self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y - i)))) is not EmptySquare:
                    return False
        # Check for pieces in the southwest direction
        elif location.x < self.location.x and location.y < self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y - i)))) is not EmptySquare:
                    return False
        return True


class KnightPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)

    def isValidMove(self, location : Position, gameBoard):
        x = self.location.x
        y = self.location.y

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == whichTurn:
            return False

        # list of all possible moves
        destinationSquares = [(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2),(x+2,y+1),(x-2,y+1),(x+2,y-1),(x-2,y-1)]

        # check if target valid for the knight
        if (location.x, location.y) not in destinationSquares:
            return False
        # check if target location is out of bounds
        if (location.x < 0 and location.x > 7) and (location.y < 0 and location.y > 7):
            return False
        if gameBoard.getPieceFromBoard(location).getColour() == self.colour:
            return False
        return True


class KingPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)

    def isValidMove(self, location : Position, gameBoard):
        dx = abs(location.x - self.location.x)
        dy = abs(location.y - self.location.y)

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == self.colour:
            return False

        if dx > 1 or dy > 1:
            return False
        # Check for pieces in the southeast direction
        if location.x > self.location.x and location.y > self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the southwest direction
        elif location.x < self.location.x and location.y > self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the northeast direction
        elif location.x > self.location.x and location.y < self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y - i)))) is not EmptySquare:
                    return False
        # Check for pieces in the northwest direction
        elif location.x < self.location.x and location.y < self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y - i)))) is not EmptySquare:
                    return False
        # Check for pieces in the east direction
        elif location.x > self.location.x:
            for i in range(1):
                if (type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y)))) is not EmptySquare):
                    return False
        # Check for pieces in the west direction
        elif location.x < self.location.x:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((location.x - i), (location.y)))) is not EmptySquare:
                    return False
        # Check for pieces in the south direction
        elif location.y > self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the north direction
        elif location.y < self.location.y:
            for i in range(1):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y - i)))) is not EmptySquare:
                    return False
        return True


class QueenPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)

    def isValidMove(self, location : Position, gameBoard):
        dx = abs(location.x - self.location.x)
        dy = abs(location.y - self.location.y)

        #make sure you're not trying to validate a move that would land on one of your own pieces
        if gameBoard.board[location.x][location.y].colour == self.colour:
            return False

        # make sure that the destination location is on a cardinal (diagonal) line of sight
        if dx != dy and (dx != 0 and dy != 0):
            return False

        # Check for pieces in the southeast direction
        if location.x > self.location.x and location.y > self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the southwest direction
        elif location.x < self.location.x and location.y > self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the northeast direction
        elif location.x > self.location.x and location.y < self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y - i)))) is not EmptySquare:
                    return False
        # Check for pieces in the northwest direction
        elif location.x < self.location.x and location.y < self.location.y:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i),(self.location.y - i)))) is not EmptySquare:
                    return False
        # Check for pieces in the east direction
        elif location.x > self.location.x:
            for i in range(1, dx):
                if (type(gameBoard.getPieceFromBoard(Position((self.location.x + i),(self.location.y)))) is not EmptySquare):
                    return False
        # Check for pieces in the west direction
        elif location.x < self.location.x:
            for i in range(1, dx):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x - i), (self.location.y)))) is not EmptySquare:
                    return False
        # Check for pieces in the south direction
        elif location.y > self.location.y:
            for i in range(1, dy):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y + i)))) is not EmptySquare:
                    return False
        # Check for pieces in the north direction
        elif location.y < self.location.y:
            for i in range(1, dy):
                if type(gameBoard.getPieceFromBoard(Position((self.location.x), (self.location.y - i)))) is not EmptySquare:
                    return False
        return True


