class Reader:

    def __init__(self, path):
        self.data = []
        with open(path) as file:
            for line in file.readlines():
                row = line.split()
                self.data.append(row)
    
    def getData(self):
        return self.data