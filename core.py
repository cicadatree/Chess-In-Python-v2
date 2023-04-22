from enum import Enum, auto


class Colour(Enum):  # Enum Class for Colour inheritance
    WHITE = auto()
    BLACK = auto()
    UNDEF = auto()

    def __str__(self):  # redefine the __str__ special function to print the Colour.WHITE as "W" and Colour.BLACK as "B" for legibility in the terminal
        if self.value == Colour.WHITE.value:
            return 'W'
        elif self.value == Colour.BLACK.value:
            return 'B'
        else:
            return ''

    __repr__ = __str__


class Position: # Position is oriented in the in-memory representation's coordinate system (x,y).
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 

    # sets the (x,y) based on the (file,rank) passed in
    def setByFileRank(self, file, rank):
        self.x = ord(file) - ord("a")
        self.y = 8 - int(rank)
        return self

    # sets the (x,y) based on the (x,y) passed in
    def setByXY(self, x, y):
        self.x = x
        self.y = y
        return self


