from collections import defaultdict
from graph import Graph
import os
d = defaultdict(list)
V, E = [int(x) for x in input('Nhập số đỉnh và cạnh trên một dòng:').split()]
for i in range(V):
    d[i] = []
graph = Graph(d)
edges = []
for i in range(E):

    u, w = [int(x) for x in input('Nhập cạnh %d trên một dòng:' %(i+1)).split()]
    graph.graph[u - 1].append(w - 1)
    graph.graph[w - 1].append(u - 1)
    edge = [u, w]
    edges.append(edge)

out = dict(zip(range(V), [0]*V))
layers = graph.bfs(0)
is_even = 0
colors = [0, 1]

for i in layers:
    for ii in i:
        out[ii] = 1*is_even
    is_even = 1-is_even
for v in range(V):
    temp_colors = colors.copy()
    for next_v in graph.graph[v]:
        try:
            temp_colors.remove(out[next_v])
        except ValueError:
            pass
    if len(temp_colors) == 0:
        out[v] = colors[-1] + 1
        colors.append(out[v])
colors_list = ['black', 'red', 'blue', 'yellow', 'green', 'white', 'pink', 'ivory', 'gray', 'cyan', 'gold', 'tan', 'brown', 'orange', 'coral', 'maroon']
try:
    os.remove('dothitomau.dot')
except FileNotFoundError:
    pass
f = open('dothitomau.dot', 'w+')
f.write('graph dothi\n{\n')
for i in range(V):
    f.write('%d [fillcolor=%s, style=filled];\n' % (i+1, colors_list[out[i]]))
for i in edges:
    f.write('%d -- %d;\n' % (i[0], i[1]))
f.write('}')
f.close()




