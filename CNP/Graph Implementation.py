from sqlalchemy import false, true


class Graph:
    def __init__(self, nVertices):
       self.nVertices = nVertices
       self.adjacencyMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self, r, c):
        self.adjacencyMatrix[r][c] = 1
        self.adjacencyMatrix[c][r] = 1
    def removeEdge(self, r, c):
        if(self.containsEdge(r, c) is False):
            return 
        self.adjacencyMatrix[r][c] = 0
        self.adjacencyMatrix[c][r] = 0
    def containsEdge(self, r, c):
        return True if(self.adjacencyMatrix[r][c] > 0) else False
        
        
    