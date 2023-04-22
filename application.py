from game import Game


class ChessApp:
    def __init__(self):
        self.exit = False
        self.isGameRunning = False
        while not self.exit:
            match self.isGameRunning:
                case True: # this is the "game" case (the game is running, so go to the game)
                    self.mainGame.gameLoop()
                case False: # this is the "menu" case (the game is not running, so go to the menu)
                    self.userInput = input("Welcome to Chess in Python. To start a new game, type: NEW. ")
                    match self.userInput:
                        case "NEW":
                            self.mainGame = Game()
                            self.isGameRunning = True


if __name__ == "__main__":
    main = ChessApp()
