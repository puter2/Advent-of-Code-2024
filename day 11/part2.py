with open('day 11\\input.txt') as file:
    stones = {}
    info = file.read()

for num in info.strip().split(' '):
    if stones.get(num):
        stones[num] += 1
    else:
        stones[num] = 1

def add_stones(dic : dict, key : str, amount : int):
    if dic.get(key):
        dic[key] += amount
    else:
        dic[key] = amount

print(stones)
blinks = 75
for _ in range(blinks):
    tmp = {}
    for key in stones.keys():
        if key == '0':
            add_stones(dic=tmp, key = '1', amount=stones.get(key))
        elif len(key) % 2 == 0:
            lenght = len(key)
            new_val1, new_val2 = str(int(key[:lenght//2])), str(int(key[(lenght//2):]))
            #print(f'val1: {new_val1}, val2: {new_val2}')
            add_stones(dic=tmp, key=new_val1, amount=stones.get(key))
            add_stones(dic=tmp, key=new_val2, amount=stones.get(key))
        else:
            add_stones(dic=tmp, key=str(2024 * int(key)), amount=stones.get(key))
    stones = tmp
    print(stones)

print(len(stones))
print(sum(stones.values()))