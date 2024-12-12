class Reader:

    def __init__(self, path):
        self.data = []
        with open(path) as file:
            for el in file.readline().split(' '):
                self.data.append(int(el))
    
    def getData(self):
        return self.data