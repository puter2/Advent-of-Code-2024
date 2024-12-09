from map import Map

class Solver:

    def __init__(self, map: Map):
        self.map = map

    def findAntinodes(self, location1: tuple, location2: tuple) -> list:
        size = self.map.getMapSize()
        loc_diff = (location2[0] - location1[0], location2[1] - location1[1])
        ant1 = (location1[0] - loc_diff[0], location1[1] - loc_diff[1])
        ant2 = (location2[0] + loc_diff[0], location2[1] + loc_diff[1])
        res = []
        if ant1[0] in range(0,size[0]) and ant1[1] in range(0,size[1]):
            res.append(ant1)
        if ant2[0] in range(0,size[0]) and ant2[1] in range(0,size[1]):
            res.append(ant2)
        return res
    
    def solve(self):
        antinodes = set()
        for freq in self.map.getFrequancies():
            #print(freq)
            locations = self.map.getFreqLocations(freq)
            for i in range(len(locations)-1):
                curr_loc = locations[i]
                for j in range(i + 1, len(locations)):
                    for antinode in self.findAntinodes(curr_loc, locations[j]):
                        antinodes.add(antinode)
        #print(antinodes)
        return len(antinodes)
