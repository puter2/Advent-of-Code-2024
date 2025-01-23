from reader import Reader
from solver import Solver

R = Reader("day 18\\input.txt")
print(R.obstacles[2911])
for i in range(1700, len(R.obstacles)):
    R.create_map(size = 71,bites = i)
    R.to_file()
    # R.display_map()

    S = Solver(R.map)
    # S.display_graph()
    S.Dijkstra()
    # S.display_graph()
    print(i,S.graph[-1][-1].best_time)
    if S.graph[-1][-1].best_time == float('inf'):
        print(R.obstacles[i-1])
        break

