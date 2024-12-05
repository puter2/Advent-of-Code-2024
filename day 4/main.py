from search import Puzzle

with open('day 4\\input.txt') as file:
    grid = []
    for line in file.readlines():
        grid.append(list(line.strip()))

for row in grid:
    print(row)

a = Puzzle()
print(a.part1(grid=grid))
print(a.part2(grid=grid))