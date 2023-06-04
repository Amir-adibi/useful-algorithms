from typing import List


class Graph:
    matrix: List[List]
    size: int

    def __init__(self, matrix=None):
        self.matrix = matrix
        self.size = len(matrix)

    def neighbors(self, vertex) -> List:
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

    def visit(self, index) -> None:
        self.visit_sequence.append(index)


class DFS(Traverser):

    def dfs(self, graph: Graph, order='PRE-ORDER') -> List:
        self.order = order
        self.visit_sequence = []
        self.marked = [False] * graph.size

        vertex = 0
        self.__perform_dfs(graph.matrix, vertex)

        return self.visit_sequence

    def __perform_dfs(self, matrix: List, vertex: int) -> None:
        if self.order == 'PRE-ORDER':
            self.visit(vertex)

        self.marked[vertex] = True
        for index in graph.neighbors(vertex):
            if not self.marked[index]:
                self.__perform_dfs(matrix, index)

        if self.order == 'POST-ORDER':
            self.visit(vertex)

    def dfs_iter(self, graph: Graph) -> List:
        self.visit_sequence = []
        self.marked = [False] * graph.size
        vertex = 0

        self.__perform_dfs_iter(vertex)

        return self.visit_sequence

    def __perform_dfs_iter(self, vertex: int) -> None:
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
    def bfs(self, graph: Graph) -> None:
        self.visit_sequence = []
        self.marked = [False] * graph.size

        vertex = 0
        self.__perform_bfs(vertex)

        return self.visit_sequence

    def __perform_bfs(self, vertex: int) -> None:
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
print(depth.dfs(graph))
print(depth.dfs(graph, order='POST-ORDER'))
print(depth.dfs_iter(graph))

breadth = BFS()
print((breadth.bfs(graph)))
