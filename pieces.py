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


class RookPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)


class BishopPiece(Piece):
    def __init__(self, colour, location: Position):
        super().__init__(colour, location)


class KnightPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)


class KingPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)


class QueenPiece(Piece):
    def __init__(self, colour, location : Position):
        super().__init__(colour, location)


