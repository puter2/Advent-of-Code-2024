from reader import Reader
from map import Map
from robot import Robot
from box import Box

r = Reader('day 15\\input.txt')

print(r.boxes)
print(r.walls)
print(r.width, r.height)
print(r.robot)
print(r.movements)

m = Map(r.walls, r.height, r.height)
m.displayMap()

robot = Robot(r.robot, m)
boxes = [Box(pos,m) for pos in r.boxes]

m.connect(boxes, robot)
# m.displayWithMovables()

# robot.move('^',boxes)
# m.displayWithMovables()
# robot.move('^',boxes)
# m.displayWithMovables()

# robot.move('>',boxes)
# m.displayWithMovables()

# robot.move('>',boxes)
# m.displayWithMovables()
# robot.move('>',boxes)
# m.displayWithMovables()

for char in r.movements:
    robot.move(char,boxes)
    #m.displayWithMovables()

m.displayWithMovables()

res = 0
for box in boxes:
    res += box.getGPS()

print(res)

# m.putObjects(boxes, robot)
# m.displayMap()