class Node:
    def __init__(self):
        self.neighbors = []
        self.prev = None
        self.best_time = float('inf')

    def add_neighbor(self, obj):
        self.neighbors.append(obj)
    


class Solver:

    def __init__(self, map : list[list[str]]):
        self.graph = []
        size = len(map)
        for i in range(size):
            row = []
            for j in range(size):
                if map[i][j] != '#':
                    cur = Node()
                    row.append(cur)
                else:
                    row.append(None)
            self.graph.append(row)
        self.graph[0][0].best_time = 0
        self.neighborhoods()

    def neighborhoods(self):
        directions = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1),
        ]
        size = len(self.graph)
        for i in range(size):
            for j in range(size):
                if self.graph[i][j] != None:
                    for dx, dy in directions:
                        if -1 < i + dx < size and -1 < j + dy < size:
                            self.graph[i][j].add_neighbor(self.graph[i + dx][j + dy])

    def display_graph(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if self.graph[i][j] != None:
                    print(f'{self.graph[i][j].best_time}', end=' ')
                else:
                    print('#',end=' ')
            print()

    def Dijkstra(self):
        unvisited = []
        size = len(self.graph)
        for i in range(size):
            for j in range(size):
                if self.graph[i][j] != None:
                    unvisited.append(self.graph[i][j])
        print(unvisited)
        while unvisited:
            cur = unvisited.pop(self.find_next(unvisited))
            if cur.best_time == float('inf'):
                break
            for neighbor in cur.neighbors:
                if neighbor in unvisited and neighbor.best_time > cur.best_time + 1:
                    neighbor.best_time = cur.best_time + 1
                    neighbor.prev = cur





    def find_next(self, tab : list[Node]):
        best = 0
        for i in range(len(tab)):
            if tab[best].best_time > tab[i].best_time:
                best = i
        return best