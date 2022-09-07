# Write your code here
import queue
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.adjMatrix)

    def dfs(self, sv, visited):
        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                self.dfs(i, visited)
                visited[i] = True
    
    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.dfs(0, visited)

        for boolVal in visited:
            if not boolVal:
                return False
        return True


# Main
arr=[int(i) for i in input().strip().split()]
V=arr[0]
E=arr[1]
g=Graph(V)

if V == 0:
    print('true')
else:
    g = Graph(V)

    for i in range(E):
        arr = [int(j) for j in input().strip().split()]
        a = arr[0]
        b = arr[1]
        g.addEdge(a, b)

    print()
    if g.isConnected():
        print('true')
    else:
        print('false')
        