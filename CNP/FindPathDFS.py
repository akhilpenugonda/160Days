import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        self.resp = []
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containsEdge(self, v1, v2):
        if(self.adjMatrix[v1][v2] > 0):
            return True
        else:
            return False
    def __str__(self):
        return str(self.adjMatrix)
    
    def __getPathDFS(self, sv, ev, visited):
        visited[sv] = True
        if(sv == ev):
            self.resp.append(sv)
            return True
        for i in range(self.nVertices):
            if(self.adjMatrix[sv][i] == 1 and visited[i] is False):
                visited[i] = True
                recResp = self.__getPathDFS(i, ev, visited)
                if(recResp):
                    self.resp.append(sv)
                    return True
        return False
    def getPathDFS(self, sv, ev):
        if(sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)):
            return list()
        visited = [False for i in range(self.nVertices)]
        self.__getPathDFS(sv, ev, visited)
        return self.resp
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])
g = Graph(V)

for i in range(E):
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)
li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])
li = g.getPathDFS(sv, ev)

if(len(li) != 0):
    for element in li:
        print(element, end = ' ')

