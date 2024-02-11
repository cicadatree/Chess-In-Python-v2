import pygame as pg
from application import main

class GameWindow:
    def __init__(self):
        pg.init()
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 800
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.caption = pg.display.set_caption("Chess")
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 36)
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.blockSize = 75 # size of grid blocks
        self.gridSize = 8 # # of grid blocks

    def drawBoard(self):

        self.startX = (self.WINDOW_WIDTH - (self.blockSize * self.gridSize)) // 2
        self.startY = (self.WINDOW_HEIGHT - (self.blockSize * self.gridSize)) // 2

        for x in range(self.startX, self.startX + self.blockSize * self.gridSize, self.blockSize):
            for y in range(self.startY, self.startY + self.blockSize * self.gridSize, self.blockSize):
                rect = pg.Rect(x, y, self.blockSize, self.blockSize)
                pg.draw.rect(self.screen, pg.Color('black') if (x // self.blockSize + y // self.blockSize) % 2 else pg.Color('white'), rect)

        borderWidth = 3
        borderRect = pg.Rect(self.startX, self.startY, self.blockSize * self.gridSize, self.blockSize * self.gridSize)
        pg.draw.rect(self.screen, pg.Color('black'), borderRect, borderWidth)

        labelOffset = 10
        for i in range(self.gridSize):
            # Draw file labels (bottom)
            fileLabel = self.font.render(self.files[i], True, pg.Color('black'))
            self.screen.blit(fileLabel, (self.startX + i * self.blockSize + self.blockSize // 2 - fileLabel.get_width() // 2, self.startY + self.gridSize * self.blockSize + labelOffset))

            # Draw rank labels (left)
            rankLabel = self.font.render(self.ranks[self.gridSize - 1 - i], True, pg.Color('black'))
            self.screen.blit(rankLabel, (self.startX - rankLabel.get_width() - labelOffset, self.startY + i * self.blockSize + self.blockSize // 2 - rankLabel.get_height() // 2))

    def drawPieces(self):
        ### iter over chessboard representation and draw each piece on the board###
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                piece = self.gameBoard.board[row][col] # get the piece info
                if piece: # If there is a piece on this square
                    # draw the piece
                    pass
                pg.draw.circle(self.screen, pg.Color('black' if piece == 'B' else 'white'),
                               (self.startX + col * self.blockSize + self.blockSize // 2,
                                self.startY + row * self.blockSize + self.blockSize // 2), 
                                self.blockSize // 2 - 10)

    def runGame(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.fill(pg.Color('white')) # full the background with white
            self.drawBoard() # draw the chessboard

            pg.display.flip() # update the full disaply surface to the screen
            self.clock.tick(60) # limit frame rate

        pg.quit()

game = GameWindow()
game.runGame()
game.drawPieces()