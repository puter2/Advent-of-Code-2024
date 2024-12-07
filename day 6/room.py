class Room:

    def __init__(self,path):
        with open(path) as file:
            self.grid = []
            for line in file.readlines():
                self.grid.append(list(line.strip()))
    
    def getStart(self):
        for row in range(len(self.grid)):
            for coulumn in range(len(self.grid[0])):
                if self.grid[row][coulumn] == '^':
                    return row, coulumn
    
    def getObstacles(self):
        obstacles = set()
        for row in range(len(self.grid)):
            for coulumn in range(len(self.grid[0])):
                if self.grid[row][coulumn] == '#':
                    obstacles.add((row,coulumn))
        return obstacles
    
    def getDimensions(self):
        return len(self.grid), len(self.grid[0])