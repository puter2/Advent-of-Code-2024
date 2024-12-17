from reader import Reader
from game import Game
from solver import Solver

r = Reader('day 13\\input.txt')

games = [Game(game['A'], game['B'], game['target']) for game in r.getData()]
print(len(games))

for game in games:
    print(Solver().solveGame(game=game))