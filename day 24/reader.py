class Reader:

    def __init__(self, path : str):
        self.values = {}
        self.formulas = []
        with open(path) as file:
            for line in file.readlines():
                if ':' in line:
                    self.values[line[:3]] = int(line.strip()[-1])
                elif '->' in line:
                    self.formulas.append(line.strip())
