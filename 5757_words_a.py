from collections import defaultdict
from graph import Graph
import sys
sys.setrecursionlimit(10000)


def search(word, words):
    n1 = len(words)-1
    n2 = 0
    if word == words[n1]:
        return n1
    while True:

        id = (n1+n2)//2
        if word == words[id]:
            break
        if word < words[id]:
            n1 = id
        else:
            n2 = id
    return id


def find_edges(words, words0, g, i):
    temp = []
    is_empty = 1
    for ii in range(len(words)-1):
        x = words[ii]
        y = words[ii+1]
        if x[:-1] == y[:-1]:
            y = y[-i-1:] + y[:-i-1]
            idy = search(y, words0)
            if is_empty:
                x = x[-i - 1:] + x[:-i - 1]
                idx = search(x, words0)

                g.add_edge(idy, idx)
                g.add_edge(idx, idy)

                temp.append(idy)
                temp.append(idx)
                is_empty -= 1
            else:
                for iii in temp:
                    g.add_edge(iii, idy)
                    g.add_edge(idy, iii)
                temp.append(idy)
        else:
            if not is_empty:
                temp = []
                is_empty = 1


path = input('Nhập đường dẫn tới file :')
with open(path, '+r') as f:
    words = sorted(f.read().split('\n'))
    words0 = words.copy()
d = defaultdict(list)
for i in range(len(words)):
    d[i] = []
graph_words = Graph(d)
find_edges(words, words0, graph_words, -1)
for i in range(4):
    for ii in range(len(words)):
        words[ii] = words[ii][1:] + words[ii][0]
    words = sorted(words)
    find_edges(words, words0, graph_words, i)
del words


# Tìm số thành phần liên thông
graph_words.dfs()


# Tìm đường đi ngắn nhất từ đỉnh u đến v

u = input('Nhập đỉnh u:')
v = input('Nhập đỉnh v:')
u = search(u, words0)
v = search(v, words0)
path = graph_words.find_path(u, v)
if len(path) == 1:
    print('Không có đường đi:')
else:
    for i in path:
        print(words0[i])

