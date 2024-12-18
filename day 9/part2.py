with open('day 9\\test.txt') as file:
    data = file.read().strip()

data = list(data)
print(data)

nums = []
counter = 0
for i in range(len(data)):
    if i % 2 == 0:
        nums.append(counter)
        counter += 1
    else:
        nums.append('space')

print(nums)

pos_last = len(data)
while pos_last > 0:
    switch = -1
    for i in range(len(nums)):
        if nums[i] == 'space' and data[i] <= data[pos_last]:
            switch = i
            break
    if switch > -1:
        if data[switch] == data[pos_last]:
            nums[switch] = nums[pos_last]
            pos_last -= 2
            nums.pop(-1)
            nums.pop(-1)
            data.pop(-1)
            data.pop(-1)
        else:
            nums.insert(switch,nums[pos_last])
            