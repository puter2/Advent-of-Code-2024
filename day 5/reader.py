class Reader:

    def __init__(self, path):
        with open(path) as file:
            self.samples = []
            self.order = {}
            for line in file.readlines():
                if '|' in line:
                    prev, next = line.strip().split('|')
                    # prev, next = int(prev), int(next)
                    if self.order.get(prev) is None:
                        self.order[prev] = [next]
                    else:
                        self.order[prev].append(next)
                else:
                    if ',' in line:
                        self.samples.append(line.strip().split(','))

    def getSamples(self):
        return self.samples
    
    def getOrder(self):
        return self.order
    