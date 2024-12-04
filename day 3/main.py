from parser import Parser

with open('day 3\\input.txt') as file:
    data = file.read()

a = Parser()
a.part1('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))m')
a.part1(data)