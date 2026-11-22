from dataclasses import dataclass
from typing import List
import heapq


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        edge = Edge(u, v, weight)
        self.edges.append(edge)

        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    # Kruskal's Algorithm
    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a
                return True

            return False

        mst = []

        for edge in sorted(self.edges, key=lambda e: e.weight):
            if union(edge.u, edge.v):
                mst.append(edge)

            if len(mst) == self.vertices - 1:
                break

        return mst

    # Prim's Algorithm
    def prim_mst(self) -> List[Edge]:
        visited = [False] * self.vertices
        heap = [(0, 0, -1)]
        mst = []

        while heap and len(mst) < self.vertices - 1:
            weight, u, parent = heapq.heappop(heap)

            if visited[u]:
                continue

            visited[u] = True

            if parent != -1:
                mst.append(Edge(parent, u, weight))

            for next_weight, v in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(
                        heap,
                        (next_weight, v, u)
                    )

        return mst


# Example
g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)


print("Kruskal MST:")
for edge in g.kruskal_mst():
    print(edge.u, "-", edge.v, ":", edge.weight)


print("\nPrim MST:")
for edge in g.prim_mst():
    print(edge.u, "-", edge.v, ":", edge.weight)