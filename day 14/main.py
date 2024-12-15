from robot import Robot
from reader import Reader
from solver import Solver

r = Reader('day 14\\input.txt')
#print(r.getData())
i=0
while True:
    # input()
    Solver().show(r.getData(), i, 101, 103)
    i += 1
    print(i)

# print(Solver().part1(r.getData(), 100, 101, 103))

# a = Robot()
# a.setPos(2,4)
# a.setVel(2,-3)
# #print(a.getVel())
# # a.move(5, 11, 7)
# # print(a.getPos())
# for _ in range(5):
#     a.move(1,11,7)
#     print(a.getPos())
