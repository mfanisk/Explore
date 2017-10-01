class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self,neighbour,weight = 0):
        self.connectedTo[neighbour] = weight

    def __str__(self):
        return str(self.id) + 'Connected to :' + str(x.id for x in self.connectedTo)

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,neighbour):
        return self.connectedTo[neighbour]

