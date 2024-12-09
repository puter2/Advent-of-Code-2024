with open('day 9\\input.txt') as file:
    data = file.read().strip()

data = list(data)
print(data)


max_num = len(data) // 2
print(max_num)

times = 0
res = 0
pnt1 = 0
pnt2 = len(data) - 1
last_num = int(max_num)
first_num = 0

while pnt1 <= pnt2:
    for _ in range(int(data[pnt1])):
        res += first_num * times
        times += 1
    pnt1 += 1
    first_num += 1
    spaces = int(data[pnt1])
    i = 0
    if pnt1 > pnt2:
        break
    while i < spaces:
        if int(data[pnt2]) != 0:
            res += last_num * times
            times += 1
            data[pnt2] = str(int(data[pnt2]) - 1)
            i += 1
        else:
            pnt2 -= 2
            last_num -= 1
            if pnt2 < pnt1:
                break
    pnt1 += 1
print(res)
