import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v1][v2] = 1
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v1][v2] = 0
    def containsEdge(self, v1, v2):
        if(self.adjMatrix[v1][v2] > 0):
            return True
        else:
            return False
    def __str__(self):
        return str(self.adjMatrix)
    def __getPathBFS(self, sv, ev, visited):
        mapp = {}
        q = queue.Queue()
        if(self.adjMatrix[sv][ev] == 1 and sv == ev):
            ans = []
            ans.append(sv)
            return ans
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            front = q.get()
            for i in range(self.nVertices):
                if(self.adjMatrix[front][i] == 1 and visited[i] is False):
                    mapp[i] = front
                    q.put(i)
                    visited[i] = True
                    if(i == ev):
                        ans = []
                        ans.append(ev)
                        value = mapp[ev]
                        while value != sv:
                            ans.append(value)
                            value = mapp[value]
                        ans.append(value)
                        return ans
        return []
    def getPathBFS(self, sv, ev):
        if(sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)):
            return list()
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)
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
li = g.getPathBFS(sv, ev)

if(len(li) != 0):
    for element in li:
        print(element, end = ' ')


















# from collections import deque
# def addEdge(v, w):
#     global adj
#     adj[v].append(w)
#     adj[w].append(v)
 
# def getPath(fromNode, toNode):
#     resp = []
#     if(fromNode == toNode):
#         return resp
    
#     foundPath = False
#     visited = [False for i in range(V)]
#     queue = deque()
#     parentDict = {}
#     visited[fromNode] = True
#     queue.append(fromNode)
#     while(len(queue) > 0):
#         s = queue.popleft()
#         (adj[s]).sort()
#         for i in adj[s]:
#             if(i == toNode):
#                 foundPath = True
#                 parentDict[i] = s
#                 break
#             if(not visited[i]):
#                 parentDict[i] = s
#                 visited[i] = True
#                 queue.append(i)
#     if(foundPath):        
#         resp.append(toNode)
#         while(resp[-1] != fromNode):
#             resp.append(parentDict[resp[-1]])            
#     return resp

# li = input().strip().split() 
# V = int(li[0]) 
# E = int(li[1]) 
# adj = [[] for i in range(V+1)]
# for i in range(E) : 
#     arr = input().strip().split() 
#     fv = int(arr[0]) 
#     sv = int(arr[1]) 
#     addEdge(fv, sv)
# u,v=map(int,input().split())
    
# path = getPath(u,v)
# for i in path:
#     print(i, end = " ")