class Reader:

    def __init__(self, path):
        with open(path) as file:
            self.edges = []
            for line in file.readlines():
                self.edges.append(line.strip().split('-'))
        