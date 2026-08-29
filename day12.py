# Graph
class Graph:
    def __init__(self):
        self.graph = {}
        
    def AddVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
              print("vertex already exists")
            
    def AddEdge(self, vertex1, vertex2, isDirected=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)
    def display(self):
        for key,value in self.graph.items():
            print(key,'===>',value)
    def remove(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)
    def isedgeexist(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            return True
        return False
    def removeEdge(self,vertex1,vertex2):
        if self.isedgeexist(vertex1,vertex2):
            if vertex1 in self.graph:
                self.graph[vertex1].remove(vertex2)
            if vertex2 in self.graph:
                self.graph[vertex2].remove(vertex1)
        else:
            print("edge does not exit")
    def dfstraversal(self,start,visited=set() ):
        visited.add(start)
        print(start,end='')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfstraversal(neighbor,visited)
    def bfstraversal(self,start):
        visited={start}
        queue=[start]
        while queue:
            current=queue.pop(0)
            print(current,end=" ")
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
g = Graph()
g.AddEdge("A", "B")
g.AddEdge("A", "C")
g.AddEdge("A", "D")
g.AddEdge("B", "C")
g.AddEdge("B", "D")
g.AddEdge("C", "D")
g.AddEdge("C", "E")
g.display()
# g.removeEdge('A','B')
# g.display()
# g.remove("D")
# g.display()
g.dfstraversal("A")
