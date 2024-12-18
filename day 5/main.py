from reader import Reader
from solver import Solver

r = Reader('day 5\\input.txt')

print(r.getOrder())
print(r.getSamples())

res = 0
for sample in r.getSamples():
    if Solver().isValid(r.getOrder(), sample):
        res += Solver().getMiddle(sample)
    # print(sample)
    # print(Solver().isValid(r.getOrder(), sample))

print(res)