from game import Game

class Solver:

    def solveGame(self, game : Game):
        min_price = float('inf')
        for a in range(101):
            for b in range(101):
                game.reset()
                game.pressA(a)
                game.pressB(b)
                if game.checkWin():
                    cur_price = a * 3 + b
                    if cur_price < min_price:
                        min_price = cur_price
                        break
        return min_price