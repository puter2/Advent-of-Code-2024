from map import Map
from solver import Solver
from solver2 import Solver2

m = Map('day 8\\input.txt')
# m.showMap()
#print(m.getFrequancies())
# for freq in m.getFrequancies():
#     print(freq, m.getFreqLocations(freq))
# print(m.getMapSize())

s = Solver(m)
print(s.solve())

s2 = Solver2(m)
print(s2.solve())
# print(s2.findAntinodes((2,1), (0,0)))