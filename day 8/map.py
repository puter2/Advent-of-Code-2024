class Map:
    
    def __init__(self, path: str):
        self.grid = []
        with open(path) as file:
            for row in file.readlines():
                self.grid.append(list(row.strip()))
    
    def showMap(self) -> None:
        for row in self.grid:
            print(row)

    def getFrequancies(self) -> set:
        frequencies = set()
        for row in self.grid:
            for el in row:
                if el != '.':
                    frequencies.add(el)
        return frequencies
    
    def getFreqLocations(self, frequency: str) -> list:
        locations = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == frequency:
                    locations.append((row,col))
        return locations
    
    def getMapSize(self):
        return len(self.grid),len(self.grid[0])