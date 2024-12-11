class Map:

    def __init__(self, path: str):
        self.map = []
        with open(path) as file:
            for row in file.readlines():
                tmp = []
                for el in row.strip():
                    tmp.append(int(el))
                self.map.append(tmp)
    
    def showMap(self) -> None:
        for row in self.map:
            print(row)

    def getSize(self) -> tuple[int,int]:
        return len(self.map), len(self.map[0])

    def findZeros(self) -> list[tuple[int,int]]:
        res = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 0:
                    res.append((i,j))
        return res
    
    def canMove(self, start: tuple, end: tuple) -> bool:
        if self.getVal(start) != None and self.getVal(end) != None:
            return self.getVal(start) == self.getVal(end) - 1
        return False
    
    def getVal(self, pos: tuple):
        if -1 < pos[0] < self.getSize()[0] and -1 < pos[1] < self.getSize()[1]:
            return self.map[pos[0]][pos[1]]
        return None