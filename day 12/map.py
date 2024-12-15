class Map:

    def __init__(self, path):
        self.grid = []
        with open(path) as file:
            for line in file.readlines():
                self.grid.append(list(''.join(line.strip())))

    def getGrid(self):
        return self.grid