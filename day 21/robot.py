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
            route = self.next.press_symbol(target_symbol)
            start = self.keypad.get_symbol(self.pos)
            res = ''
            for char in route:
                res += self.keypad.find_route(start, char) + 'A'
                start = char
            return res

    def show_state(self):
        tmp = []
        for i in range(len(self.keypad.grid)):
            row = []
            for j in range(len(self.keypad.grid[0])):
                row.append(self.keypad.grid[i][j])
                if i == self.pos[1] and j == self.pos[0]:
                    row[j] = 'X'
            tmp.append(row)
            
        # tmp = self.keypad.grid.copy()
        # tmp[self.pos[1]][self.pos[0]] = 'X'
        res = ''
        for row in tmp:
            res += str(row) + '\n'
        return res
    
    def push_button(self):
        if self.next:
            directions = {
            '<':(-1,0),
            '^':(0,-1),
            '>':(1,0),
            'v':(0,1),
            }
            symbol = self.keypad.get_symbol(self.pos)
            if symbol == 'A':
                self.next.push_button()
            else:
                dx, dy = directions[symbol]
                self.next.move_pos(dx,dy)

    def me_make_move(self, symbol):
        directions = {
        '<':(-1,0),
        '^':(0,-1),
        '>':(1,0),
        'v':(0,1),
        }
        if symbol != 'A':
            dx, dy = directions[symbol]
            self.move_pos(dx, dy)
        else:
            self.push_button()

    def move_pos(self, dx, dy):
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)