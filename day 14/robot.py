class Robot:

    def __init__(self):
        self.pos_x, self.pos_y, self.vx, self.vy = 0, 0, 0, 0
    
    def setPos(self, x : int, y : int):
        self.pos_x, self.pos_y = x, y

    def setVel(self, x : int, y : int):
        self.vx, self.vy = x, y

    def setPos(self, pos : tuple):
        self.pos_x, self.pos_y = pos[0], pos[1]

    def setVel(self, vel : tuple):
        self.vx, self.vy = vel[0], vel[1]
    
    def getPos(self):
        return self.pos_x, self.pos_y
    
    def getVel(self):
        return self.vx, self.vy

    def move(self, time, width, heigth):
        self.pos_x = (self.pos_x + (self.vx * time)) % (width)
        self.pos_y = (self.pos_y + (self.vy * time)) % (heigth)

    
