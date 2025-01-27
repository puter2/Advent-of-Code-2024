from reader import Reader
from graph import Graph

R = Reader('day 23\\test.txt')

G = Graph(R.edges)
#part1
#create find all triangles
triangles = []
verts = list(G.vertices.keys())
for i in range(len(verts)):
    for j in range(i+1,len(verts)):
        for z in range(j + 1, len(verts)):
            if G.check_if_triangle(verts[i],verts[j],verts[z]):
                triangles.append([verts[i],verts[j],verts[z]])
print(triangles)
print(len(triangles))
res = []
for triangle in triangles:
    if triangle[0][0] == 't' or triangle[1][0] == 't' or triangle[2][0] == 't':
        res.append(triangle)
print(res)
print(len(res))
'''
ka-co
ta-co
de-co
ta-ka
de-ta
ka-de'''
print(G.check_if_clique(['ka','co','ta','de']))