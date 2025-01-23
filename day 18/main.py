from reader import Reader
from solver import Solver

R = Reader("day 18\\input.txt")
print(R.obstacles)

R.create_map(size = 71,bites = 1024)
R.to_file()
# R.display_map()

S = Solver(R.map)
S.display_graph()
S.Dijkstra()
S.display_graph()