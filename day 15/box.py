from movable import Movable

class Box(Movable):

    def __init__(self, x, y, map):
        super().__init__(x, y, map)

    def __init__(self, pos, map):
        super().__init__(pos, map)

    def getGPS(self):
        return self.y * 100 + self.x