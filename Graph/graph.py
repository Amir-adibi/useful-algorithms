from typing import List


class Graph:
    matrix: List[List]
    size: int

    def __init__(self, matrix=None):
        self.matrix = matrix
        self.size = len(matrix)

    def neighbors(self, vertex):
        neighbors = []
        IS_CONNECTED = 1

        for v in range(self.size):
            if self.matrix[vertex][v] == IS_CONNECTED and v != vertex:
                neighbors.append(v)

        return neighbors


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

        vertex = 0
        self.__perform_dfs(graph.matrix, vertex)

        self.print_visit_sequence()

    def __perform_dfs(self, matrix: List, vertex: int):
        if self.order == 'PRE-ORDER':
            self.visit(vertex)

        self.marked[vertex] = True
        for index in graph.neighbors(vertex):
            if not self.marked[index]:
                self.__perform_dfs(matrix, index)

        if self.order == 'POST-ORDER':
            self.visit(vertex)

    def dfs_iter(self, graph: Graph):
        self.visit_sequence = []
        self.marked = [False] * graph.size
        vertex = 0

        self.__perform_dfs_iter(vertex)

        self.print_visit_sequence()

    def __perform_dfs_iter(self, vertex):
        stack = [vertex]

        while len(stack):
            vertex = stack.pop()
            if not self.marked[vertex]:
                self.visit(vertex)
                self.marked[vertex] = True

                for index in graph.neighbors(vertex):
                    if not self.marked[index]:
                        stack.append(index)


class BFS(Traverser):
    def bfs(self, graph: Graph):
        self.visit_sequence = []
        self.marked = [False] * graph.size

        vertex = 0
        self.__perform_bfs(vertex)

        self.print_visit_sequence()

    def __perform_bfs(self, vertex: int):
        queue = [vertex]

        while len(queue):
            vertex = queue.pop(0)
            if not self.marked[vertex]:
                self.visit(vertex)
                self.marked[vertex] = True
                for w in graph.neighbors(vertex):
                    queue.append(w)


graph = Graph([[1, 1, 1, 1, 0],
               [1, 1, 0, 1, 0],
               [1, 0, 1, 1, 0],
               [1, 1, 1, 1, 1],
               [0, 0, 0, 1, 1]])

depth = DFS()
depth.dfs(graph)
depth.dfs(graph, order='POST-ORDER')
depth.dfs_iter(graph)

breadth = BFS()
breadth.bfs(graph)
