from reader import Reader
from solver import Stone

r = Reader('day 11\\input.txt')

stones = []
for val in r.getData():
    stones.append(Stone(val=val))

#print([stone.getVal() for stone in stones])
tmp = []
times = 75
# print(type(Stone(1).blink()))
# stones = [Stone(0)]
for i in range(times):
    print(i)
    tmp = []
    for stone in stones:
        for res in stone.blink():
            tmp.append(res)
    stones = tmp.copy()
    #print([stone.getVal() for stone in stones])
#print([stone.getVal() for stone in stones])
print(len(stones))
print(2**75)