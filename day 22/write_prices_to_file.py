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
# secrets = [int(num.strip()) for num in fileinput.input('day 22\\input.txt')]
# print(secrets)
secrets = [1, 2, 3, 2024]
prices = []
last = []
with open('day 22\\pricestest.txt', 'w') as file:
    for secret in secrets:
        cur = secret
        prices.append(cur % 10)
        for _ in range(2000):
            new = next_number(cur)
            # print(new)
            prices.append(new % 10)
            cur = new
        file.write(str(prices)[1:-1] + '\n')
        prices = []
        last.append(cur)

# print(sum(last))