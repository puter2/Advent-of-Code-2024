from keypad import Keypad
from robot import Robot

l = Keypad()
print(l.find_route('A','8'))
d = Keypad('directional')
print(d.find_route('A', '<'))


r1 = Robot(Keypad())
r2 = Robot(Keypad('directional'), r1)
r3 = Robot(Keypad('directional'), r2)

with open('day 21\\input.txt') as file:
    codes = []
    for line in file:
        codes.append(line.strip())
res = 0
inputs = []
for code in codes:
    moves = ''
    for char in code:
        moves += r3.press_symbol(char)
    print(f'{code}: {moves} lenght = {len(moves)} num = {int(code[:-1])} res = {len(moves) * int(code[:-1])}')
    inputs.append(moves)
    res += len(moves) * int(code[:-1])
# print(r2.press_symbol('0'))
print(res)

# lenghts = [74, 70, 63, 74, 72]
# nums = [671, 83, 582, 638, 341,]
# res = 0
# for l, n in zip(lenghts, nums):
#     res += l*n
# print(res)

# print(r1.move_pos(-1,-1))
# print(r1.show_state())
for code in inputs:
    for char in code:
        print(code)
        print(char)
        print(r1.show_state())
        print(r2.show_state())
        print(r3.show_state())
        r3.me_make_move(char)
        input()

print(r1.show_state())
print(r2.show_state())
# print(r1.show_state())
# print(r2.show_state())
# r2.me_make_move('<')
# print(r1.show_state())
# print(r2.show_state())
# r2.me_make_move('A')
# print(r1.show_state())
# print(r2.show_state())


def find_seq(target, nums):
    
    l = [51,51,51,51,51]
    res = 0
    for x, y in zip(l, nums):
        res += x*y
    def get_next(l):
        limit = [74, 70, 76, 74, 72]
        pos = 0
        while l[pos] == limit[pos]:
            pos += 1
        for i in range(pos):
            l[i] = 51
        l[pos] += 1

    while res != target:
        get_next(l)
        print(l)
        res = 0
        for x, y in zip(l, nums):
            res += x*y
    return l

# print(find_seq(163920,nums))
