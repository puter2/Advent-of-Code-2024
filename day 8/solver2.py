from map import Map

class Solver2:

    def __init__(self, map: Map):
        self.map = map

    def findAntinodes(self, location1: tuple, location2: tuple) -> set:
        size = self.map.getMapSize()
        loc_diff = (location2[0] - location1[0], location2[1] - location1[1])
        cur_loc = (location1[0], location1[1])
        antinodes = set()
        while -1 < cur_loc[0] < size[0] and -1 < cur_loc[1] < size[1]:
            antinodes.add(cur_loc)
            cur_loc = (cur_loc[0] + loc_diff[0], cur_loc[1] + loc_diff[1])
        cur_loc = (location1[0], location1[1])
        while -1 < cur_loc[0] < size[0] and -1 < cur_loc[1] < size[1]:
            antinodes.add(cur_loc)
            cur_loc = (cur_loc[0] - loc_diff[0], cur_loc[1] - loc_diff[1])
        return antinodes
    
    def solve(self):
        antinodes = set()
        for freq in self.map.getFrequancies():
            #print(freq)
            locations = self.map.getFreqLocations(freq)
            for i in range(len(locations)-1):
                curr_loc = locations[i]
                for j in range(i + 1, len(locations)):
                    #print(curr_loc, locations[j], self.findAntinodes(curr_loc, locations[j]))
                    for antinode in self.findAntinodes(curr_loc, locations[j]):
                        antinodes.add(antinode)
        #print(antinodes)
        return len(antinodes)
