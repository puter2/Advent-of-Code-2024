class Robot:

    def __init__(self):
        self.pos_x, self.pos_y, self.vx, self.vy = 0, 0, 0, 0
    
    def setPos(self, x, y):
        self.pos_x, self.pos_y = x, y

    def setVel(self, x, y):
        self.vx, self.vy = x, y
    
    def getPos(self):
        return self.pos_x, self.pos_y
    
    def getVel(self):
        return self.vx, self.vy

    def move(self, time, width, heigth):
        self.pos_x = (self.pos_x + (self.vx * time)) % (width + 1)
        self.pos_y = (self.pos_y + (self.vy * time)) % (heigth + 1)

    
