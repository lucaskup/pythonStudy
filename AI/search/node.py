from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.edges = []
        self.father = None
    def bind(self,cost,n):
        self.edges.append(Edge(cost,n))
        n.edges.append(Edge(cost,self))
    def __str__(self):
        return self.value
    def getSons(self):
        l = []
        for i in range(len(self.edges)):
            l.append(self.edges[i].node.value)
        return l


class Edge:
    def __init__(self, cost, node):
        self.cost = cost
        self.node = node
class Graph:
    def __init__(self):
        self.nodes = {}
    def addNode(self,n):
        self.nodes[n.value] = n
    def contains(self,value):
        return value in self.nodes

class BFS:
    def __init__(self, g):
        self.graph = g
    def search(self,initialValue,targetValue):
        r = []
        visited = set()
        queue = deque()
        current = self.graph.nodes[initialValue]
        queue.append(current)
        while len(queue) > 0:
            current = queue.popleft()
            print(current.value,current.father,current.getSons())
            if current.value == targetValue:
                break
            if not current.value in visited:
                visited.add(current.value)
                for e in current.edges:
                    if not e.node.value in visited and e.node not in queue:
                        e.node.father = current
                    queue.append(e.node)

        if current.value == targetValue:
            while current.value !=  initialValue:
                r.append(current.value)
                current = current.father
            r.append(current.value)
        return r
