class Guard:

    def __init__(self, room):
        self.room = room

    def traverse(self):
        obstacles = self.room.getObstacles()
        pos = self.room.getStart()
        borders = self.room.getDimensions()
        directions = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1),
        ]
        dir_pnt = 0
        seen = set()
        while -1 < pos[0] < borders[0] and -1 < pos[1] < borders[1]:
            dx, dy = directions[dir_pnt]
            next_pos = (pos[0] + dx, pos[1] + dy)
            if next_pos not in obstacles:
                #print(pos)
                seen.add(pos)
                pos = next_pos
            else:
                dir_pnt += 1
                dir_pnt %= 4
        return len(seen)