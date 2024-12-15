from map import Map

class Solver:

    def findRegion(self, map : Map, x : int, y : int):
        grid = map.getGrid()
        directions = [
                    (0,1),
                    (1,0),
                    (0,-1),
                    (-1,0)
                ]
        symbol = grid[x][y]
        region  = [(x,y)]
        q = [(x,y)]
        while q:
            cur = q.pop(0)
            for dx, dy in directions:
                pass