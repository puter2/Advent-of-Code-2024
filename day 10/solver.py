from reader import Map
class Solver:

    def __init__(self, map: Map):
        self.map = map


    def evaluatePath(self, pos: tuple):
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        reached = [pos]
        res = set()
        while reached:
            curr = reached.pop(0)
            if self.map.getVal(curr) == 9:
                res.add(curr)
            else:
                for dx, dy in directions:
                    if self.map.canMove(curr, (curr[0] + dx, curr[1] + dy)):
                        reached.append((curr[0] + dx, curr[1] + dy))
        return len(res)
    
    def part1(self):
        starts = self.map.findZeros()
        scores = []
        for zero in starts:
            scores.append(self.evaluatePath(zero))
        return sum(scores)