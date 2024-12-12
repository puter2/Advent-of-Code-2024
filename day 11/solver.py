class Stone:

    def __init__(self, val):
        self.val = val

    def blink(self):
        if self.checkFirstRule():
            return [Stone(1)]
        elif self.checkSecondRule():
            val_as_str = str(self.getVal())
            lenght = len(val_as_str)
            #print(lenght)
            new_val1, new_val2 = int(val_as_str[:lenght//2]), int(val_as_str[(lenght//2):])
            return [Stone(new_val1), Stone(new_val2)]
        else:
            return [Stone(self.getVal() * 2024)]


    def checkFirstRule(self):
        return self.getVal() == 0

    def checkSecondRule(self):
        return len(str(self.getVal())) % 2 == 0

    def getVal(self):
        return self.val
    