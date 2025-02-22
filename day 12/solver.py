from map import Map
directoins = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]
def divide_into_regions(m : map):
        unvisited = []
        grid = m.grid.copy()
        print(grid)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                unvisited.append((x,y))
        regions = []
        while unvisited:
            cur = unvisited.pop()
            q = [cur]
            zone = {cur}
            while q:
                cur2 = q.pop(0)
                for dx, dy in directoins:
                    new = (cur2[0]+dx, cur2[1]+dy)
                    if new in unvisited and grid[cur[1]][cur[0]] == grid[new[1]][new[0]]:
                        unvisited.remove(new)
                        zone.add(new)
                        q.append(new)
            regions.append(zone)
            #print(regions)
        
        return regions

def calculate_fence(zone : list):
    fence = []
    for lot in zone:
        for dx, dy in directoins:
            new = (lot[0]+dx, lot[1]+dy)
            if new not in zone:
                fence.append(new)
    return fence

