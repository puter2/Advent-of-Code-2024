from reader import Reader
from solver import Solver

r = Reader('day 5\\input.txt')

print(r.getOrder())
print(r.getSamples())

res = 0
res2 = 0
for sample in r.getSamples():
    if Solver().isValid(r.getOrder(), sample):
        res += Solver().getMiddle(sample)
    else:
        fixed = Solver().fixSample(r.getOrder(), sample)
        # print(Solver().fixSample(r.getOrder(), sample))
        res2 += Solver().getMiddle(fixed)
    # print(sample)
    # print(Solver().isValid(r.getOrder(), sample))

print(res)
print(res2)