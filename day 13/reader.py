class Reader:

    def __init__(self, path):
        self.data = []
        with open(path) as file:
            game = {}
            i = 0
            for line in file.readlines():
                if i==0:
                    X = int(line.split(' ')[2][2:-1])
                    Y = int(line.split(' ')[3][2:-1])
                    game['A'] = (X,Y)
                elif i==1:
                    X = int(line.split(' ')[2][2:-1])
                    Y = int(line.split(' ')[3][2:-1])
                    game['B'] = (X,Y)
                elif i==2:
                    X = int(line.split(' ')[1][2:-1])
                    Y = int(line.split(' ')[2][2:-1])
                    game['target'] = (X,Y)
                else:
                    self.data.append(game.copy())
                    i = 0
                    continue
                i+=1
            self.data.append(game.copy())
    def getData(self):
        return self.data