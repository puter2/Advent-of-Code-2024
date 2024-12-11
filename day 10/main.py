from reader import Map
from solver import Solver

r = Map('day 10\\input.txt')

r.showMap()
print(r.findZeros())
print(r.getSize())
print(r.canMove((0,0), (0,1)))

s = Solver(r)

print(s.evaluatePath((0,0)))
print(s.part1())