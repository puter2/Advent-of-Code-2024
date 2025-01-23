class Reader:

    def __init__(self, path):
        self.obstacles = []
        with open(path) as file:
            for line in file.readlines():
                self.obstacles.append(line.strip())
    
    def create_map(self, size = 70, bites = -1):
        self.map = [ ['.' for _ in range(size)] for a in range(size)]
        if bites == -1 or bites > len(self.obstacles):
            bites = len(self.obstacles)
        for i in range(bites):
            # print(self.obstacles[i])
            self.map[int(self.obstacles[i].split(',')[-1])][int(self.obstacles[i].split(',')[0])] = '#'
    
    def display_map(self):
        for l in self.map:
            print(l)


    def to_file(self):
        with open('day 18\\map.txt','w') as file:
            for l in self.map:
                for el in l:
                    file.write(el)
                file.write('\n')