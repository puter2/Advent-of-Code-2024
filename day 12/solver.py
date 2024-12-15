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
                new_x = cur[1] + dx
                new_y = cur[0] + dy
                if -1 < new_x < len(grid[0]) and -1 < new_y < len(grid) and grid[new_x][new_y] == symbol and (new_x,new_y) not in region:
                    q.append((new_x,new_y))
                    region.append((new_x,new_y))
        return region                
