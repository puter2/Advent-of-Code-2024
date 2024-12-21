from record import Record

class Reader:

    def __init__(self, path):
        self.data = []
        with open(path) as file:
            i = 0
            counter = 0
            for line in file.readlines():
                for char in line.strip():
                    if i % 2 == 0:
                        self.data.append(Record(int(char), counter))
                        counter += 1
                    else:
                        self.data.append(Record(int(char), '.'))
                    i += 1

