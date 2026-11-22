from typing import List
import heapq


class ShortestPath:

    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.graph[u].append((v, weight))

    # Dijkstra's Algorithm
    def dijkstra(self, src: int) -> List[int]:
        INF = float('inf')
        distance = [INF] * self.vertices
        distance[src] = 0

        priority_queue = [(0, src)]

        while priority_queue:
            current_distance, u = heapq.heappop(priority_queue)

            if current_distance > distance[u]:
                continue

            for v, weight in self.graph[u]:
                new_distance = current_distance + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    heapq.heappush(
                        priority_queue,
                        (new_distance, v)
                    )

        return distance

    # Bellman-Ford Algorithm
    def bellman_ford(self, src: int) -> List[int]:
        INF = float('inf')
        distance = [INF] * self.vertices
        distance[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            updated = False

            for u, v, weight in self.edges:

                if distance[u] != INF:
                    new_distance = distance[u] + weight

                    if new_distance < distance[v]:
                        distance[v] = new_distance
                        updated = True

            if not updated:
                break

        # Check for negative-weight cycle
        for u, v, weight in self.edges:
            if distance[u] != INF:
                if distance[u] + weight < distance[v]:
                    return ["Negative Cycle"]

        return distance


# Example
sp = ShortestPath(5)

sp.add_edge(0, 1, 4)
sp.add_edge(0, 2, 1)
sp.add_edge(2, 1, 2)
sp.add_edge(1, 3, 1)
sp.add_edge(2, 3, 5)
sp.add_edge(3, 4, 3)


print("Dijkstra:", sp.dijkstra(0))
print("Bellman-Ford:", sp.bellman_ford(0))