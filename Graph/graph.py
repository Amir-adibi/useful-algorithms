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
    visit_sequence: List
    order: str

    def visit(self, index):
        self.visit_sequence.append(index)

    def print_visit_sequence(self):
        print(self.visit_sequence)


class DFS(Traverser):

    def dfs(self, graph: Graph, order='PRE-ORDER'):
        self.order = order
        self.visit_sequence = []
        self.marked = [False] * graph.size

        vertex = Vertex(0, graph.matrix[0])
        self.__perform_dfs(graph.matrix, vertex)

        self.print_visit_sequence()

    def __perform_dfs(self, matrix: List, vertex: Vertex):
        if self.order == 'PRE-ORDER':
            self.visit(vertex.index)
        self.marked[vertex.index] = True

        for index in vertex.neighbors:
            if not self.marked[index]:
                self.__perform_dfs(matrix, Vertex(index, matrix[index]))

        if self.order == 'POST-ORDER':
            self.visit(vertex.index)

    def dfs_iter(self, graph: Graph):
        self.visit_sequence = []
        self.marked = [False] * graph.size

        vertex = Vertex(0, graph.matrix[0])
        stack = [vertex]

        while len(stack):
            vertex = stack.pop()
            if not self.marked[vertex.index]:
                self.visit(vertex.index)
                self.marked[vertex.index] = True

                for index in vertex.neighbors:
                    if not self.marked[index]:
                        stack.append(Vertex(index, graph.matrix[index]))

        self.print_visit_sequence()


graph = Graph([[1, 1, 1, 1, 0],
               [1, 1, 0, 1, 0],
               [1, 0, 1, 1, 0],
               [1, 1, 1, 1, 1],
               [0, 0, 0, 1, 1]])

traverse = DFS()
traverse.dfs(graph)
traverse.dfs(graph, order='POST-ORDER')
traverse.dfs_iter(graph)
