from map import Map
from solver import Solver
m = Map('day 12\\test.txt')
print(m.getGrid())
print(Solver().findRegion(m, 0, 0))