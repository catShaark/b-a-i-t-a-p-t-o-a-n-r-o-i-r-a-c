from collections import defaultdict
import heapq


class Graph:

    def __init__(self, graph):
        self.graph = graph

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):

        visited = [False] * len(self.graph)
        queue = [s]
        visited[s] = True
        out = []
        n = 0
        m = 1
        while queue:
            temp = []

            for x in range(m):

                s = queue.pop(0)
                temp.append(s)
                for i in self.graph[s]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
                        n += 1
                m = n
                n = 0
            out.append(temp)
        return out

    def explore(self, v, visited):

        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.explore(i, visited)

    def dfs(self):
        V = len(self.graph)
        visited = [False] * V
        n = 0
        for i in range(V):
            if not visited[i]:
                self.explore(i, visited)
                n += 1
        print('Số thành phần liên thông là:', n)

    def find_path(self, u, v):
        visited = [False] * len(self.graph)
        history = [u]
        visited[u] = True
        path = [v]
        n = 0

        while n != len(history):
            s = history[n]
            if float(s).is_integer():
                history.append(str(n))
            n += 1

            for i in self.graph[s]:

                if i == v:
                    idex = len(history) - 1
                    while True:
                        if type(history[idex]) == str:
                            idex = int(history[idex])
                            path.append(int(history[idex]))
                        if idex == 0:
                            return path
                        idex -= 1

                if not visited[i]:
                    history.append(i)
                    visited[i] = True
        return path.reverse()

    def dfs2(self):
        V = len(self.graph)
        visited = [False] * V

        pres = dict(zip([i for i in range(V)], [None]*V))
        n = [0, 1]
        for i in range(V):
            if not visited[i]:
                self.explore2(i, visited, pres, n)
        return pres

    def explore2(self, vertex, visited, pres, n):

        n[0] += 1
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                self.explore2(i, visited, pres, n)
        n[0] += 1
        pres[vertex] = n[0]

    def explore4(self, v, visited, connect):
        visited[v] = True
        connect.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.explore4(i, visited, connect)

    def dijkstra(self, s):
        V = len(self.graph())
        prevs = dict(zip(range(V), [0]*V))
        dists = [1000] * V
        dists[s] = 0
        queue = [[0, s]]
        while queue:
            u = heapq.heappop(queue)
            for v in self.graph[u]:
                if dists[v[0]] > dists[u] + v[1]:
                    dists[v[0]] = dists[u] + v[1]
                    prevs[v[0]] = u
                    heapq.heappush(queue, [dists[v[0]], v[0]])
        return prevs, dists

    def dijkstra2(self, s):
        V = len(self.graph())
        prevs = dict(zip(range(V), [0] * V))
        dists = [1000] * V
        dists[s] = 0
        queue = [[0, s]]
        while queue:
            u = heapq.heappop(queue)
            for v in self.graph[u]:
                if dists[v[0]] > dists[u] + v[1]:
                    dists[v[0]] = dists[u] + v[1]
                    prevs[v[0]] = u
                    heapq.heappush(queue, [dists[v[0]], v[0]])
        return prevs

    def dijkstra1(self, s):
        V = len(self.graph())
        dists = [1000] * V
        dists[s] = 0
        queue = [[0, s]]
        while queue:
            u = heapq.heappop(queue)
            for v in self.graph[u]:
                if dists[v[0]] > dists[u] + v[1]:
                    dists[v[0]] = dists[u] + v[1]

                    heapq.heappush(queue, [dists[v[0]], v[0]])
        return dists

