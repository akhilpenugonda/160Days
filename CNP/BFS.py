# Write your code hereimport queue
import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def __dfsHelper(self, sv, visited):
        print(sv) #starting Vertex
        visited[sv] = True
        for i in range(self.nVertices):
            if(self.adjMatrix[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i, visited)
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if(visited[i] is False):
                self.__dfsHelper(0, visited)
    def hasPathHelper(self, v1, v2, visited):
        visited[v1] = True
        #print(v1, v2)
        if(v1 == v2):
            return True
        for i in range(self.nVertices):
            if(self.adjMatrix[v1][i] > 0 and visited[i] is False):
                return self.hasPathHelper(i,v2, visited)
        return False
    def hasPath(self, v1, v2):
        if(self.nVertices == 0):
            return False
        visited = [False for i in range(self.nVertices)]
        return self.hasPathHelper(v1, v2, visited)
    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while(q.empty() is False):
            u = q.get()
            print(u, end = " ")
            for i in range(self.nVertices):
                if(self.adjMatrix[u][i] == 1 and visited[i] is False):
                    q.put(i)
                    visited[i] = True 
    def bfs(self):
        if(self.nVertices == 0):
            return
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if(visited[i] == False):
                self.__bfsHelper(i, visited)
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
                        return ans
        return []
    def getPathBfs(self, sv, ev):
        if(sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)):
            return list()
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)
    def removeEdge(self, v1, v2):
        if(self.containsEdge(v1, v2) is False):
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containsEdge(self, v1, v2):
        return True if(self.adjMatrix[v1][v2] > 0) else False
    def __str__(self):
        return str(self.adjMatrix)

inp = list(int(i) for i in input().split())
g = Graph(inp[0])
for i in range(inp[1]):
    edge = list(int(i) for i in input().split())
    g.addEdge(edge[0], edge[1])
# print("DFS")
# g.dfs()
# print("BFS")
g.bfs()
print(g.getPathBfs(0,2))
