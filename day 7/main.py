from reader import Reader
from solver import Solver

r = Reader('day 7\\input.txt')
print(r.getData())

s = Solver()
# test = ['*'] * 5
# end = ['+'] * (len(test))
# while test != end:
#     s.nextConfig(configuration=test)
#     print(test)
# print(s.testNoOrder(292, [11,6,16,20], ['+','*','+']))
print(s.solve(r.getData()))