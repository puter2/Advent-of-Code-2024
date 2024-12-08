from reader import Reader
from solver import Solver
from solver2 import Solver2

r = Reader('day 7\\input.txt')
print(r.getData())

s = Solver()
test = ['*'] * 5
end = ['+'] * (len(test))
while test != end:
    s.nextConfig(configuration=test)
    d = {'*':0, '|':1, '+':2}
    print([d[char] for char in test])

#print(s.testNoOrder(292, [11,6,16,20], ['+','*','+']))
print(s.solve(r.getData()))

s2 = Solver2()
print(s2.solve(r.getData()))