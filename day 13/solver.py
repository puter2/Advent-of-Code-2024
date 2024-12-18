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
    
    def solveGame2(self, game : Game):
        min_price = float('inf')
        game.correctTarget()
        limit = self.findRange(game)
        print(limit)
        for a in range(limit):
            for b in range(limit):
                game.reset()
                game.pressA(a)
                game.pressB(b)
                if game.checkWin():
                    cur_price = a * 3 + b
                    if cur_price < min_price:
                        min_price = cur_price
                        break
        return min_price
    
    def findRange(self, game: Game):
        x_trgt, y_trgt = game.getTarget()
        Ax, Ay = game.getA()
        limit_A = min(x_trgt // Ax + 1, y_trgt // Ay + 1)
        Bx, By = game.getB()
        limit_B = min(x_trgt // Bx + 1, y_trgt // By + 1)
        
        return max(limit_A, limit_B)
    
    def costFor10Tril(self, game : Game):
        Ax, Ay = game.getA()
        Bx, By = game.getB()
        combined_movement = (Ax + Bx, Ay + By)
        target = 10000000000000
        print(target // combined_movement[0] + 1, target // combined_movement[1] + 1)
        return min(target // combined_movement[0] + 1, target // combined_movement[1] + 1)