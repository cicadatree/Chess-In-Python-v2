from game import Game


class ChessApp:
    def __init__(self):
        self.player1 = ()
        self.player2 = ()
        self.mainGame = Game()
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
                            self.colourChoice = input("Which colour do you want to play as? (Enter \"w\" or \"b\") ")
                            if self.colourChoice == "w":
                                self.mainGame = Game()
                                self.isGameRunning = True
                            elif self.colourChoice == "b":
                                #TODO: implement ai move first (player chose to play black). In the meantime,
                                print("sorry, this has not been implemented yet. Try again.")
                                continue
                            else:
                                continue


if __name__ == "__main__":
    main = ChessApp()
