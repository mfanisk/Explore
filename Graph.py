import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertexCount = 0

    def addVertex(self,vertexKey):
        self.vertexCount = self.vertexCount + 1
        newVertex = Vertex(vertexKey)
        self.vertices[vertexKey] = newVertex
        return newVertex

    def getVertex(self,vertexKey):
        if vertexKey in self.vertices:
            return self.vertices[vertexKey]
        else:
            return None

    def __contains__(self, vertexKey):
        return vertexKey in self.vertices

    def addEdge(self,start,end,cost = 0):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)
        self.vertices[start].addNeighbour(self.vertices[end],cost)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())