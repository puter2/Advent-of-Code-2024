class Reader:

    def __init__(self, path):
        self.data = []
        with open(path) as file:
            for line in file.readlines():
                strings = line.split()
                pos = strings[0][2:]
                vel = strings[1][2:]
                robot = {'p' : (int(pos[0 : pos.find(',')]),int(pos[pos.find(',') + 1 : ])),
                         'v' : (int(vel[0 : vel.find(',')]),int(vel[vel.find(',') + 1 : ]))
                         }
                self.data.append(robot)
    
    def getData(self):
        return self.data