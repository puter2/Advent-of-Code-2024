class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def make_neighbors(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)

class Graph:
    
    def __init__(self, edges : list):
        self.edges = edges.copy()
        self.vertices = {}
        for edge in edges:
            for vert in edge:
                self.vertices[vert] = Node(name=vert)
        tmp_dic = {}
        for edge in edges:
            for vert in edge:
                if tmp_dic.get(vert) == None:
                    tmp_dic[vert] = []
            tmp_dic[edge[0]].append(edge[1])
            tmp_dic[edge[1]].append(edge[0])
        for key in tmp_dic.keys():
            for vert in tmp_dic[key]:
                self.vertices[key].make_neighbors(self.vertices[vert])

    def check_if_triangle(self, vert1, vert2, vert3):
        v1, v2, v3 = self.vertices[vert1], self.vertices[vert2], self.vertices[vert3]
        if v1 in v2.neighbors and v1 in v3.neighbors and v2 in v3.neighbors:
            return True
        else:
            return False
        
    def check_if_clique(self, verts):
        for i in range(len(verts)):
            cur = self.vertices[verts[i]]
            for j in range(i+1, len(verts)):
                new = self.vertices[verts[j]]
                if cur not in new.neighbors:
                    return False
        return True

    def find_biggest_clique(self):
        biggest = []
        for vert in self.vertices.keys():
            for i in range(len(self.vertices[vert].neighbors)):
                tmp = [vert, self.vertices]
        