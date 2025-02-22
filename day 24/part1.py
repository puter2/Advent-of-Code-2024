from reader import Reader
from solver import Solver

R = Reader("day 24/input.txt")

values, formulas = R.values, R.formulas

print(values)
print(formulas)
print(values['y02'])

ops = {'AND' : lambda x, y : x and y,
       'XOR' : lambda x, y : x ^ y,
       'OR' : lambda x, y : x or y}

Solver.run(values, formulas)

res = {key : val for key, val in values.items() if key[0] == 'z'}

result = ''
for val in sorted(res,reverse=True):
    result += str(int(res[val]))
print(result)

print(int(result,2))