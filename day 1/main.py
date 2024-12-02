def part1():
    with open('day 1\\input.txt') as file:
        list1 = []
        list2 = []
        for line in file.readlines():
            id1, id2 = line.split()[0], line.split()[-1]
            list1.append(int(id1))
            list2.append(int(id2))
    list1.sort()
    list2.sort()
    res = 0
    for el1, el2 in zip(list1,list2):
        res += abs(el1-el2)
    return res

def part2():
    with open('day 1\\input.txt') as file:
        list1 = []
        list2 = []
        count = {}
        for line in file.readlines():
            id1, id2 = line.split()[0], line.split()[-1]
            list1.append(int(id1))
            list2.append(int(id2))
            if count.get(int(id2)):
                count[int(id2)] += 1
            else:
                count[int(id2)] = 1
    res = 0
    # print(list1)
    # print(count)
    for el in list1:
        # print(el,count.get(el))
        if count.get(el)!=None:
            res += el*int(count.get(el))
    return res

# print(part1())
print(part2())