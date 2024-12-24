def next_number(number):
    return step3(step2(step1(number)))

def step1(number):
    res = number * 64
    res = mix(res, number)
    res = prune(res)
    return res

def step2(number):
    res = number // 32
    res = mix(res, number)
    res = prune(res)
    return res

def step3(number):
    res = number * 2048
    res = mix(res, number)
    res = prune(res)
    return res

def mix(number, secret):
    return number ^ secret

def prune(number):
    return number % 16777216

import fileinput
secrets = [int(num.strip()) for num in fileinput.input('day 22\\input.txt')]
print(secrets)
# secrets = [1, 10, 100, 2024]
last = []
for secret in secrets:
    cur = secret
    for _ in range(2000):
        new = next_number(cur)
        # print(new)
        cur = new
    last.append(cur)

print(sum(last))