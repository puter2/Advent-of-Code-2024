class Map:

    def __init__(self, walls, height, width):
        self.grid = []
        for _ in range(height):
            self.grid.append(['.'] * width)
        for x, y in walls:
            self.grid[y][x] = '#'

    def putObjects(self, boxes, robot):
        for box in boxes:
            x, y = box.getPos()
            self.grid[y][x] = 'O'

        x, y = robot.getPos()
        self.grid[y][x] = '@'

    def putObjects(self):
        for box in self.boxes:
            x, y = box.getPos()
            self.grid[y][x] = 'O'

        x, y = self.robot.getPos()
        self.grid[y][x] = '@'

    def connect(self, boxes, robot):
        self.boxes = boxes
        self.robot = robot

    def reset(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != '#':
                    self.grid[i][j] = '.'

    def getBoxesLoc(self):
        res = []
        for i in range(self.grid):
            for j in range(self.grid[0]):
                if self.grid[i][j] == 'O':
                    res.append((i,j))
        return res

    def displayMap(self):
        for row in self.grid:
            print(''.join(row))
        self.reset()

    def isWall(self, x, y):
        return self.grid[y][x] == '#'
    
    def displayWithMovables(self):
        self.putObjects()
        self.displayMap()