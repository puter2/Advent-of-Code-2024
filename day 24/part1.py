from reader import Reader

R = Reader("day 24/input.txt")

values, formulas = R.values, R.formulas

print(values)
print(formulas)
print(values['y02'])

ops = {'AND' : lambda x, y : x and y,
       'XOR' : lambda x, y : x ^ y,
       'OR' : lambda x, y : x or y}

print(ops['AND'](True,False))
while formulas:
    tmp = []
    for formula in formulas:
        var1, var2, res, op = formula.split(' ')[0], formula.split(' ')[2], formula.split(' ')[-1], formula.split(' ')[1]
        if values.get(var1)!=None and values.get(var2)!=None:
            values[res] = ops[op](values.get(var1), values.get(var2))
        else:
            tmp.append(formula)
    formulas = tmp.copy()
    print(formulas)

res = {key : val for key, val in values.items() if key[0] == 'z'}

result = ''
for val in sorted(res,reverse=True):
    result += str(int(res[val]))
print(result)

print(int(result,2))