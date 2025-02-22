class Solver:

    def run(values : dict, formulas :list):
        ops = {'AND' : lambda x, y : x and y,
       'XOR' : lambda x, y : x ^ y,
       'OR' : lambda x, y : x or y}
        while formulas:
            tmp = []
            for formula in formulas:
                var1, var2, res, op = formula.split(' ')[0], formula.split(' ')[2], formula.split(' ')[-1], formula.split(' ')[1]
                if values.get(var1)!=None and values.get(var2)!=None:
                    values[res] = ops[op](values.get(var1), values.get(var2))
                else:
                    tmp.append(formula)
            formulas = tmp.copy()