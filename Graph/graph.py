from typing import List


class Graph:
    matrix: List[List]
    size: int

    def __init__(self, matrix=None):
        self.matrix = matrix
        self.size = len(matrix)


class Vertex:
    index: int
    neighbors: List

    # the row argument indicates the row of the original matrix which corresponds to this vertex.
    def __init__(self, index, row):
        self.index = index
        self.__find_neighbors(row)

    def __find_neighbors(self, row):
        self.neighbors = []
        IS_CONNECTED = 1

        for v in range(len(row)):
            if row[v] == IS_CONNECTED and v != self.index:
                self.neighbors.append(v)



class Traverser:
    marked: List

    # TODO: check again this line
    visit_sequence: List

    def __init__(self):
        self.visit_sequence = []

    def dfs(self, graph: Graph):
        self.marked = [False] * graph.size
        vertex = Vertex(0, graph.matrix[0])

        self.__perform_dfs(graph.matrix, vertex)
        self.__print_visit_sequence()

    def __perform_dfs(self, matrix, vertex):
        self.marked[vertex.index] = True
        self.__visit(vertex.index)

        for neighbor in vertex.neighbors:
            if not self.marked[neighbor]:
                self.__perform_dfs(matrix, Vertex(neighbor, matrix[neighbor]))

    # TODO: check again this line
    def __visit(self, index):
        self.visit_sequence.append(index)

    def __print_visit_sequence(self):
        print(self.visit_sequence)


graph = Graph([[1, 1, 1, 1, 0],
               [1, 1, 0, 1, 0],
               [1, 0, 1, 1, 0],
               [1, 1, 1, 1, 1],
               [0, 0, 0, 1, 1]])

traverse = Traverser()
traverse.dfs(graph)
