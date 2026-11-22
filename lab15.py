from typing import List


class GraphBacktracker:

    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n = len(graph)

    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.n

        def is_safe(vertex, color):
            for i in range(self.n):
                if self.graph[vertex][i] == 1 and colors[i] == color:
                    return False
            return True

        def backtrack(vertex):
            if vertex == self.n:
                return True

            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors

        return []


    def hamiltonian_cycle(self) -> List[int]:
        path = [-1] * self.n
        path[0] = 0

        def is_safe(vertex, position):
            if self.graph[path[position - 1]][vertex] == 0:
                return False

            if vertex in path:
                return False

            return True

        def backtrack(position):
            if position == self.n:
                return self.graph[path[position - 1]][path[0]] == 1

            for vertex in range(1, self.n):
                if is_safe(vertex, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = -1

            return False

        if backtrack(1):
            return path + [path[0]]

        return []


# Example graph
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

solver = GraphBacktracker(graph)

print("Graph Coloring:", solver.graph_coloring(3))
print("Hamiltonian Cycle:", solver.hamiltonian_cycle())