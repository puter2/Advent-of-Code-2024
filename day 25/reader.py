from key import Key
from lock import Lock

def read(filepath):
    with open(file=filepath) as file:
        cur = ''
        locks = []
        keys = []
        tmp = [0, 0, 0, 0, 0]
        for line in file.readlines():
            if line == '\n':
                if cur == 'key':
                    keys.append(Key(tmp))
                else:
                    locks.append(Lock(tmp))
                cur = ''
                continue
            if cur == '':
                if '.' in line:
                    cur = 'key'
                    tmp = [-1, -1, -1, -1, -1]
                else:
                    cur = 'lock'
                    tmp = [0, 0, 0, 0, 0]
            else:
                for i in range(len(line.strip())):
                    if line[i] == '#':
                        tmp[i] += 1 
        if cur == 'key':
            keys.append(Key(tmp))
        else:
            locks.append(Lock(tmp))
    return locks, keys