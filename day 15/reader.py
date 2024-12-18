class Reader:

    def __init__(self, path):
        with open(path) as file:
            self.boxes = []
            self.movements = ''
            self.walls = []
            counter = 0
            for line in file.readlines():
                if '#' in line:
                    for i in range(len(line)):
                        if line[i] == 'O':
                            self.boxes.append((i, counter))
                        elif line[i] == '@':
                            self.robot = (i, counter)
                        elif line[i] == '#':
                                self.walls.append((i,counter))
                elif '<' in line or 'v' in line or '>' in line or '^' in line:
                    self.movements += line.strip()
                counter += 1
            print(self.walls)
            self.width = self.walls[-1][0] + 1
            self.height = self.walls[-1][1] + 1
