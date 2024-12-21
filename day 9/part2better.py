from reader import Reader
from record import Record
from solver import Solver

r = Reader('day 9\\input.txt')
res = Solver().solve(r.data)
print(Solver().encode(res))
print(Solver().checksum(res))