class Puzzle:

    def part1(self,grid):
        #grid = 2D array
        rows = len(grid)
        columns = len(grid[0])
        res = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 'X':
                    down = True if row + 3 < rows else False
                    up = True if row - 3 > -1 else False
                    left = True if column - 3 > -1  else False
                    right = True if column +3 < rows else False
                    if right:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row][column+i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if left:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row][column-i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if down:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row+i][column]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if up:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row-i][column]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if up and right:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row-i][column+i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if up and left:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row-i][column-i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if down and right:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row+i][column+i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)
                    if down and left:
                        tmp = ''
                        for i in range(4):
                            tmp += grid[row+i][column-i]
                        if tmp == 'XMAS':
                            res += 1
                            #print(row,column)

        return res

    def part2(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        res = 0
        for row in range(1, rows-1):
            for column in range(1, columns-1):
                if grid[row][column] == 'A':
                    mas = 0
                    if grid[row-1][column-1] == 'M' and grid[row+1][column+1] == 'S':
                        mas += 1
                    if grid[row-1][column+1] == 'M' and grid[row+1][column-1] == 'S':
                        mas += 1
                    if grid[row+1][column-1] == 'M' and grid[row-1][column+1] == 'S':
                        mas += 1
                    if grid[row+1][column+1] == 'M' and grid[row-1][column-1] == 'S':
                        mas += 1
                    if mas >= 2:
                        res += 1
        return res