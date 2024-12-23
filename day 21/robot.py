from keypad import Keypad

class Robot:

    def __init__(self, keypad : Keypad, next=None):
        self.keypad = keypad
        self.pos = self.keypad.find_symbol('A')
        self.next = next

    def get_cur_symbol(self):
        return self.keypad.get_symbol(self.pos)

    def press_symbol(self, target_symbol):
        if self.next == None:
            old_pos = self.pos.copy()
            self.pos = self.keypad.find_symbol(target_symbol)
            return self.keypad.find_route(self.keypad.get_symbol(old_pos), target_symbol) + 'A'
        else:
            route = self.next.order_movement(target_symbol)
            start = self.keypad.get_symbol(self.pos)
            res = ''
            for char in route:
                res += self.keypad.find_route(start, char) + 'A'
                start = char
            return res

    def move_child(self):
        pass