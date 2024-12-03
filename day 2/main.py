from reader import Reader
from solver import Solver

a = Reader()
data = a.read('day 2\\input.txt')
#print(data)
b = Solver()
print(b.part1(data=data))

#test
# print(b.part1(
#     data=[
#         [1,2,3,4],
#         [5,4,3,2],
#         [2,3,1,2],
#         [1,5,9]]))