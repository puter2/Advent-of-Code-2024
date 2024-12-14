from robot import Robot

a = Robot()
a.setPos(2,4)
a.setVel(2,-3)
#print(a.getVel())
a.move(1, 11, 7)
print(a.getPos())