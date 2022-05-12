# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from abc import ABC, abstractmethod
from enum import Enum
from math import inf
from copy import copy


class Color(Enum):
    WHITE = 0
    BLUE = 1


class Node:
    def __init__(self, key):
        self.key = key
        self.color = Color.WHITE

    def __hash__(self):
        return hash(self.key)


class Edge:

    def __init__(self, node1=None, node2=None, weight=0):
        if node1 is None and node2 is None:
            self.edge = tuple()
        else:
            self.edge = (node1, node2, weight)

    def __str__(self):
        return f"{self.edge[0]} - {self.edge[2]} > {self.edge[1]}"


# Interfejs, z którego korzystać będą: klasa reprezentująca listę sąsiedztwa i klasę reprezentującą macierz sąsiedztwa
class Graph(ABC):
    @abstractmethod
    def insertVertex(self, node):
        pass

    @abstractmethod
    def insertEdge(self, node1, node2, edge):
        pass

    @abstractmethod
    def deleteVertex(self, node):
        pass

    @abstractmethod
    def deleteEdge(self, node1, node2):
        pass

    @abstractmethod
    def getVertexIdx(self, node):
        pass

    @abstractmethod
    def getVertex(self, vertex_idx):
        pass

    @abstractmethod
    def neighbours(self, vertex_idx):
        pass

    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def edges(self):
        pass


class AdjacencyList(Graph):
    def __init__(self, vertexesList=[]):
        self.graph = []
        self.edgesList = []
        if not vertexesList:  # Gdy graf jest pusty
            self.adjacencyListDict = {}
        else:
            self.adjacencyListDict = {key: value for key, value in
                                      zip(vertexesList, [self.order() for key in vertexesList])}

    def insertVertex(self, node):
        if node.key not in self.adjacencyListDict:
            self.graph.append([])
            self.adjacencyListDict[node.key] = self.order()

    def insertEdge(self, node1, node2, weight):
        edge_to_add = (node1.key, node2.key, weight)
        edge_to_add_2 = (node2.key, node1.key, weight)
        if edge_to_add not in self.edgesList:
            self.edgesList.append(edge_to_add)
            self.edgesList.append(edge_to_add_2)
            self.graph[self.adjacencyListDict[node1.key]].append(node2.key)
            self.graph[self.adjacencyListDict[node2.key]].append(node1.key)

    def deleteVertex(self, node):
        self.graph.pop(self.adjacencyListDict[node.key])
        for vertex in self.graph:
            try:
                index = vertex.index(node.key)
                vertex.pop(index)
            except ValueError:
                pass
        val = self.adjacencyListDict[node.key]
        del self.adjacencyListDict[node.key]
        for key, value in self.adjacencyListDict.items():
            if value >= val+1:
                self.adjacencyListDict[key] -= 1

        for edge in self.edgesList:
            if edge[0] == node.key or edge[1] == node.key:
                self.edgesList.remove((edge[0], edge[1]))
                self.edgesList.remove((edge[1], edge[0]))

    def deleteEdge(self, node1, node2):
        try:
            for elem in self.edgesList:
                if elem[0] == node1.key and elem[1] == node2.key:
                    self.edgesList.remove(elem)
                if elem[0] == node2.key and elem[1] == node1.key:
                    self.edgesList.remove(elem)
            for vertex1 in self.graph[self.adjacencyListDict[node1.key]]:
                if vertex1 == node2.key:
                    self.graph[self.adjacencyListDict[node1.key]].remove(vertex1)
            for vertex2 in self.graph[self.adjacencyListDict[node2.key]]:
                if vertex2 == node1.key:
                    self.graph[self.adjacencyListDict[node2.key]].remove(vertex2)

        except ValueError:
            if node1.key not in self.adjacencyListDict.keys() and node2.key not in self.adjacencyListDict.keys():
                print(f"{node1.key} and {node2.key} not in graph!")
            elif node2.key not in self.adjacencyListDict.keys():
                print(f"{node2.key} not in graph!")
            else:
                print(f"{node1.key} not in graph!")

    def getVertexIdx(self, node):
        return self.adjacencyListDict[node.key] if node.key in self.adjacencyListDict.keys() else None

    def getVertex(self, vertex_idx):
        for key, value in self.adjacencyListDict.items():
            if vertex_idx == self.adjacencyListDict[key]:
                return key
        return None

    def neighbours(self, vertex_idx):
        if vertex_idx not in self.adjacencyListDict.values():
            raise Exception("No such vertex index!")
        return [self.adjacencyListDict[key] for key in self.graph[vertex_idx]]

    def order(self):
        return len(self.adjacencyListDict.keys())

    def size(self):
        return len(self.edgesList)

    def edges(self):
        return self.edgesList

    def MST_algorithm(self, key):

        def get_key(val):
            for key_, value in self.adjacencyListDict.items():
                if val == value:
                    return key_
            raise Exception("Key not found in get_key() method!")

        MST_graph = AdjacencyList()
        for k in self.adjacencyListDict.keys():
            MST_graph.insertVertex(Node(k))

        intree = [0 for _ in range(len(self.graph))]
        distance = [inf for _ in range(len(self.graph))]
        parent = [-1 for _ in range(len(self.graph))]
        v = self.adjacencyListDict[key]
        distance[v] = 0
        while intree[v] == 0:
            intree[v] = 1
            for w in self.neighbours(v):
                weight = self.edgesList[self.edgesList.index([item for item in self.edgesList if item[0] ==
                                                              get_key(v) and item[1] == get_key(w)][0])][2]
                if weight < distance[w] and intree[w] == 0:
                    distance[w] = weight
                    parent[w] = v

            v = 1
            dist = inf
            for i in range(1, len(self.adjacencyListDict.keys())):
                if intree[i] == 0 and dist > distance[i]:
                    dist = distance[i]
                    v = i
            MST_graph.insertEdge(Node(get_key(parent[v])), Node(get_key(v)), distance[v])
            MST_graph.insertEdge(Node(get_key(v)), Node(get_key(parent[v])), distance[v])
            print(intree)
            print(distance)
        return MST_graph, sum(distance)


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        if not nbrs:
            print(end=";")
        for j in nbrs:
            print(g.getVertex(j), end=";")
        print()
    print("-------------------")


if __name__ == "__main__":
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]
    graph = AdjacencyList()
    for elem in graf:
        graph.insertVertex(Node(elem[0]))
        graph.insertVertex(Node(elem[1]))
    for val1, val2, val3 in graf:
        graph.insertEdge(Node(val1), Node(val2), val3)
    printGraph(graph)
    print(graph.graph)
    print("edges")
    print(graph.edgesList)
    MST, suma = graph.MST_algorithm('A')
    printGraph(MST)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
