from map import Map

class Movable:

    global directions
    directions = {
        '>' : (1,0),
        '^' : (0,-1),
        'v' : (0,1),
        '<' : (-1,0)
    }

    def __init__(self, x, y, map : Map):
        self.x = x
        self.y = y
        self.map = map

    def __init__(self, pos, map):
        self.x = pos[0]
        self.y = pos[1]
        self.map = map
    
    def getPos(self):
        return self.x, self.y

    def move(self, direction, boxes):
        if not self.checkMovement(direction,boxes):
            return
        dx, dy = directions[direction]
        new_cords = (self.x + dx, self.y + dy)
        for box in boxes:
            if new_cords == box.getPos():
                box.move(direction, boxes)
                break
        self.x += dx
        self.y += dy


    def checkMovement(self, direction, boxes : list):
        dx, dy = directions[direction]
        new_cords = (self.x + dx, self.y + dy)
        for box in boxes:
            if new_cords == box.getPos():
                return box.checkMovement(direction, boxes)
        if self.map.isWall(new_cords[0], new_cords[1]):
            return False
        else: 
            return True

