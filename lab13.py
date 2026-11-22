from typing import List

class TSPSolver:

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 1:
            return 0

        dp = [[float('inf')] * n for _ in range(1 << n)]
        dp[1][0] = 0

        for mask in range(1 << n):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue

                for v in range(n):
                    if mask & (1 << v):
                        continue

                    new_mask = mask | (1 << v)

                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + dist_matrix[u][v]
                    )

        full_mask = (1 << n) - 1

        answer = float('inf')

        for u in range(1, n):
            answer = min(
                answer,
                dp[full_mask][u] + dist_matrix[u][0]
            )

        return int(answer)


# Example
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()

print("Minimum tour cost:", solver.solve_tsp(dist_matrix))