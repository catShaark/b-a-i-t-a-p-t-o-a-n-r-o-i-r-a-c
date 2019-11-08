from graph import Graph
from collections import defaultdict
import numpy as np


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


def tarjan(v):
    global next, next_group
    work = [(v, 0)]
    while work:
        v, i = work[-1]
        del work[-1]
        if i == 0:
            index[v] = next
            low_link[v] = next
            next += 1
            stack.append(v)
            on_stack[v] = True
        recurse = False
        for j in range(i, len(adj[v])):
            w = adj[v][j]
            if index[w] is None:
                work.append((v, j+1))
                work.append((w, 0))
                recurse = True
                break
            elif on_stack[w]:
                low_link[v] = min(low_link[v], index[w])
        if recurse:
            continue
        if index[v] == low_link[v]:
            com = []
            while True:
                w = stack[-1]
                del stack[-1]
                on_stack[w] = False
                com.append(w)
                group_id[w] = next_group
                if w == v:
                    break
            groups.append(com)
            next_group += 1
        if work:
            w = v
            v, _ = work[-1]
            low_link[v] = min(low_link[v], low_link[w])


path = input('Nhập đường dẫn tới file:')
with open(path, '+r') as f:
    words = sorted(f.read().split('\n'))

    n_words = len(words)
    X = np.full((n_words, 26), 0.1)
    Y = np.zeros((26, n_words))
    for i in range(n_words):
        word = words[i]
        for letter in word:
            temp = ord(letter)-95
            X[i][temp-2] = temp**word.count(letter)

    for i in range(n_words):
        word = words[i][1:]
        for letter in word:
            temp = ord(letter)-95
            Y[temp-2][i] = 1/(temp**word.count(letter))
    Z = X.dot(Y)


o = np.where(Z == np.round(Z))

dt = defaultdict(list)

graph_words = Graph(dt)
for x, y in zip(o[0], o[1]):

    graph_words.graph[x].append(y)
adj = graph_words.graph
next = 0
index = [None] * 5757
low_link = [None] * 5757
on_stack = [False] * 5757
stack = []
next_group = 0
groups = []
group_id = {}

for v in range(5757):
    if index[v] is None:
        tarjan(v)


# Tìm số thành phần liên thông mạnh
print('Số thành phần liên thông mạnh là:', len(groups))
print(len(o[0]))

# Tìm các đỉnh thuộc cùng thành phần liên thồng mạnh
x = input('Nhập đỉnh x:')
x = search(x, words)
id = group_id[x]
for i in groups[id]:
    print(words[i])

# Tìm đường đi ngắn nhất từ u đến v
u = input('Nhập đỉnh u:')
v = input('Nhập đỉnh v:')
u = search(u, words)
v = search(v, words)
path = graph_words.find_path(v, u)
if len(path) == 1:
    print('Không có đường đi:')
else:
    for i in path:
        print(words[i])











