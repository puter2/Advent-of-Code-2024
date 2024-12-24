class Keypad:

    def __init__(self, k_type = 'numeric'):
        self.grid = []
        self.type = k_type
        if k_type == 'numeric':
            self.grid = [
                ['7', '8', '9'],
                ['4', '5', '6'],
                ['1', '2', '3'],
                [None, '0', 'A']
            ]
        elif k_type == 'directional':
            self.grid = [
                [None, '^', 'A'],
                ['<', 'v', '>']
            ]
    

    def find_symbol(self, symbol : str):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == symbol:
                    return [j, i]
        return [-1, -1]
    
    def is_pos_valid(self, x, y):
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid) and self.grid[y][x] != None

    def find_route(self, symbol1, symbol2):
        start = self.find_symbol(symbol1)
        finish = self.find_symbol(symbol2)
        move = (finish[0] - start[0], finish[1] - start[1])
        hor = '>' * move[0] if move[0]>0 else '<' * abs(move[0])
        vert = 'v' * move[1] if move[1]>0 else '^' * abs(move[1])
        if None in self.grid[start[1]]:
            return vert+hor
        else:
            return hor+vert
        
    def get_symbol(self, pos):
        return self.grid[pos[1]][pos[0]]
    