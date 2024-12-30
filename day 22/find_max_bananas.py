with open('day 22\\prices.txt') as file:
    prices = []
    for line in file.readlines():
        cur = []
        for char in line.strip().split(' '):
            cur.append(int(char[0]))
        prices.append(cur)



def next_comb(comb):
    for i in range(len(comb)):
        if comb[i] != 9:
            pos = i
            break
    for i in range(pos):
        comb[i] = -9
    comb[pos] += 1

def buy_bananas(comb, prices):
    curr = [prices[1] - prices[0],
            prices[2] - prices[1],
            prices[3] - prices[2],]
    for i in range(4,len(prices)):
        curr.append(prices[i] - prices[i-1])
        # print(curr)
        if comb == curr:
            return prices[i]
        else:
            curr.pop(0)
    return 0

def is_combo_valid(comb):
    for i in range(3):
        if abs(comb[i] + comb[i+1]) > 9:
            return False
    if abs(sum(comb[:3])) > 9 or abs(sum(comb[1:4])) > 9 or abs(sum(comb)) > 9:
        return False
    return True
    
combo = [-9, -9, -9, -9]

# while combo != [9,9,9,9]:
#     next_comb(combo)
#     print(combo)
# print(buy_bananas([-2,1,-1,3],prices[3]))

best = 0
best_combo = []
while combo != [9,9,9,9]:
    score = 0
    if is_combo_valid(combo):
        for price in prices:
            score += buy_bananas(combo,price)
        if score > best:
            best = score
            best_combo = [i for i in combo]
    next_comb(combo)
    print(f'{combo}, best : {best}, best_com : {best_combo}')
print(best, best_combo)