# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
from abc import ABC, abstractmethod
from polska import *
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.next_ = None

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, node1=None, node2=None):
        if node1 is None and node2 is None:
            self.edge = tuple()
        else:
            self.edge = (node1, node2)

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


class AdjacencyMatrix(Graph):
    def __init__(self, vertexesList=[]):
        self.graph = []  # Tworzymy graf w postaci listy list
        self.edgesList = []  # Będzie przechowywać krotki w postaci (węzeł1, węzeł2, wartość krawędzi)
        if not vertexesList:
            self.adjacencyMatrixDict = {}
        else:
            self.adjacencyMatrixDict = {key: value for key, value in
                                        zip(vertexesList, [self.order() for key in vertexesList])}

    def insertVertex(self, node):
        if node.key not in self.adjacencyMatrixDict:
            self.graph.append([])
            for verse in self.graph:
                if self.graph.index(verse) == 0:
                    verse.append(0)
                else:
                    self.graph[self.graph.index(verse)] = self.graph[0].copy()
            self.adjacencyMatrixDict[node.key] = self.order()

    def insertEdge(self, node1, node2, edge=None):
        if node1.key in self.adjacencyMatrixDict.keys() and node2.key in self.adjacencyMatrixDict.keys():
            self.graph[self.adjacencyMatrixDict[node1.key]][self.adjacencyMatrixDict[node2.key]] = 1
            self.edgesList.append((node1.key, node2.key))

    def deleteVertex(self, node):
        if node.key in self.adjacencyMatrixDict.keys():
            index_to_remove = self.adjacencyMatrixDict.pop(node.key)
            for key, value in self.adjacencyMatrixDict.items():
                if value >= index_to_remove + 1:
                    self.adjacencyMatrixDict[key] -= 1

            for vertex in self.graph:
                vertex.pop(index_to_remove)
            self.graph.pop(index_to_remove)

            for edge in self.edgesList:
                if edge[0] == node.key or edge[1] == node.key:
                    self.edgesList.remove((edge[0], edge[1]))
                    self.edgesList.remove((edge[1], edge[0]))

    def deleteEdge(self, node1, node2):
        if node1.key in self.adjacencyMatrixDict.keys() and node2.key in self.adjacencyMatrixDict.keys():
            self.graph[self.adjacencyMatrixDict[node1.key]][self.adjacencyMatrixDict[node2.key]] = 0
            self.graph[self.adjacencyMatrixDict[node2.key]][self.adjacencyMatrixDict[node1.key]] = 0
            self.edgesList.remove((node1.key, node2.key))
            self.edgesList.remove((node2.key, node1.key))

    def getVertexIdx(self, node):
        return self.adjacencyMatrixDict[node.key] if node.key in self.adjacencyMatrixDict.keys() else None

    def getVertex(self, vertex_idx):
        for key, value in self.adjacencyMatrixDict.items():
            if vertex_idx == self.adjacencyMatrixDict[key]:
                return key
        return None

    def neighbours(self, vertex_idx):
        neighbours = []
        for vertex in range(len(self.graph[vertex_idx])):
            if self.graph[vertex_idx][vertex] == 1:
                neighbours.append([value for key, value in self.adjacencyMatrixDict.items() if value == vertex][0])
        return neighbours

    def order(self):
        return len(self.adjacencyMatrixDict.keys())

    def size(self):
        return len(self.edgesList)

    def edges(self):
        return self.edgesList


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

    def insertEdge(self, node1, node2, edge):
        edge_to_add = (node1.key, node2.key)
        if edge_to_add not in self.edgesList:
            self.edgesList.append(edge_to_add)
            self.graph[self.adjacencyListDict[node1.key]].append(node2.key)

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
            self.edgesList.remove((node1.key, node2.key))
            self.edgesList.remove((node2.key, node1.key))
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


def test(AdjacencyRepresentation):
    graph = AdjacencyRepresentation()
    for val in polska:
        graph.insertVertex(Node(val[2]))
    for val1, val2 in graf:
        graph.insertEdge(Node(val1), Node(val2), None)
    graph.deleteVertex(Node('K'))
    graph.deleteEdge(Node('W'), Node('E'))
    draw_map(graph.edges())


if __name__ == "__main__":
    print("Adjacency Matrix:\n")
    test(AdjacencyMatrix)

    print("\n\nAdjacency List:\n")
    test(AdjacencyList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
