from reader import Reader
from game import Game
from solver import Solver

r = Reader('day 13\\input.txt')

games = [Game(game['A'], game['B'], game['target']) for game in r.getData()]
print(len(games))

tokens = 0

for game in games:
    tmp = Solver().solveGame(game)
    if tmp != float('inf'):
        tokens += tmp

print(tokens)
