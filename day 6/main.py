from room import Room
from guard import Guard

r = Room('day 6\\input.txt')

print(r.grid)
print(r.getStart())
print(r.getObstacles())
print(r.getDimensions())

g = Guard(r)

print(g.traverse())