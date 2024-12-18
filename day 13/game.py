class Game:

    def __init__(self, A, B, target):
        self.A = A
        self.B = B
        self.target = target
        self.reset()

    def getA(self):
        return self.A
    
    def getB(self):
        return self.B

    def reset(self):
        self.claw_x = self.claw_y = 0

    def pressA(self, times = 1):
        self.claw_x += self.A[0] * times
        self.claw_y += self.A[1] * times

    def pressB(self, times = 1):
        self.claw_x += self.B[0] * times
        self.claw_y += self.B[1] * times

    def getPos(self):
        return self.claw_x, self.claw_y
    
    def getTarget(self):
        return self.target
    
    def checkWin(self):
        return self.getTarget() == self.getPos()
    
    def correctTarget(self):
        self.target = (self.target[0] + 10000000000000, self.target[1] + 10000000000000)