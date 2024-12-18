from movable import Movable

class Robot(Movable):

    def __init__(self, x, y, map):
        super().__init__(x, y, map)

    def __init__(self, pos, map):
        super().__init__(pos, map)
    