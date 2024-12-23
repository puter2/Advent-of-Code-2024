from keypad import Keypad
from robot import Robot

l = Keypad()
print(l.find_route('A','8'))

r = Robot(l)
for char in '029A':
    print(r.press_symbol(char))
    print(r.get_cur_symbol())