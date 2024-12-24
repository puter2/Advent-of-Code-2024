with open('day 22\\prices.txt') as file:
    prices = []
    for line in file.readlines():
        cur = []
        for char in line.strip().split(' '):
            cur.append(int(char[0]))
        prices.append(cur)



def next_comb(comb):
    pass
    for i in range(len(comb)):
        if comb[i] != 9:
            pos = i
            break
    for i in range(pos):
        comb[i] = -9
    comb[pos] += 1

def get_bananas_from_prices(comb, prices):
    pass
    
combo = [-9, -9, -9, -9]

while combo != [9,9,9,9]:
    next_comb(combo)
    print(combo)