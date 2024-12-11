from reader import Map
from solver import Solver

r = Map('day 10\\test1.txt')

r.showMap()
print(r.findZeros())
print(r.getSize())
print(r.canMove((1,1), (1,2)))

s = Solver(r)

print(s.evaluatePath((0,0)))
print(s.part1())