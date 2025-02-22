from map import Map
import solver
m = Map('day 12\\input.txt')
print(m.getGrid())
print(zones := solver.divide_into_regions(m=m))
print(solver.calculate_fence(zones[0]))
res = 0
for zone in zones:
    fence = solver.calculate_fence(zone)
    print(f'{len(zone)} * {len(fence)} = {len(zone)*len(fence)}')
    res += len(zone)*len(fence)
    # tmp = [['.' for _ in range(15)] for _ in range(15)]
    # for x, y in zone:
    #     tmp[y][x] = 'A'
    # for x, y in fence:
    #     tmp[y][x] = '*'
    # for z in tmp:
    #     print(''.join(z))  

print(res)