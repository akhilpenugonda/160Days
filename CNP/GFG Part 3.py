# Write your code hereimport queue
import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def removeEdge(self, v1, v2):
        if(self.containsEdge(v1, v2) is False):
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containsEdge(self, v1, v2):
        return True if(self.adjMatrix[v1][v2] > 0) else False
    def __str__(self):
        return str(self.adjMatrix)
    def longest_cable(self,graph):
        start = 0 # Arbitrary starting node.
        farthest_city, farthest_distance = self._find_farthest_city(start, graph)
        farthest_city, farthest_distance = self._find_farthest_city(farthest_city, graph)
        return farthest_distance
    def _find_farthest_city(self,city, graph):
        # Total cable lengths from city to each other city.
        distances = self._get_distances(city, graph)
        
        # Find longest cable from city.
        max_distance = -float("inf")
        for other_city, distance in enumerate(distances):
            if distance > max_distance:
                max_distance = distance
                farthest_city = other_city
        return farthest_city, max_distance
    def _get_distances(self,city, graph, visited, distances):
        def _depth_first_search(city, graph, visited, distances):
            visited[city] = True
            for next_city, next_distance in enumerate(graph[city]):
                if next_distance is not None and not visited[next_city]:
                    distances[next_city] = distances[city] + graph[city][next_city]
                    _depth_first_search(next_city, graph, visited, distances)

        distances = [-float("inf")] * len(graph)
        visited = [False] * len(graph)
        distances[city] = 0
        _depth_first_search(city, graph, visited, distances)
        return distances
    def __getPathBFS (self, sv, ev, visited) :
        mapp = {}
        q = queue.Queue()
        if self.adjMatrix[sv] [ev] == 1 and sv == ev :
            ans = [] 
            ans.append(sv)
            return ans
        q.put(sv) 
        visited [sv] = True
        while q.empty() is False:
            front = q.get()
            for i in range(self.nVertices) :
                if self.adjMatrix[front][1] == 1 and visited[i] is False: 
                    mapp[i]= front
                    q.put(1)
                    visited[i] = True
                    if( i == ev):
                        ans = []
                        ans.append(ev)
                        value = mapp[ev]
                        while (value != sv):
                            ans.append(value)
                            value = mapp[value]
                            ans.append(value)
                        ans.append(value)
                        return ans
        return []
    def getPathBfs(self, sv, ev):
        if(sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)):
            return list()
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)
inp = list(int(i) for i in input().split())
g = Graph(inp[0])
for i in range(inp[1]):
    edge = list(int(i) for i in input().split())
    g.addEdge(edge[0], edge[1])
# print("DFS")
# g.dfs()
# print("BFS")
g.longest_cable([[0,1],[1,2],[2,3]])
