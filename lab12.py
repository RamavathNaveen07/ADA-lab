from typing import List


# Floyd-Warshall Algorithm
def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)

    distance = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(
                    distance[i][j],
                    distance[i][k] + distance[k][j]
                )

    return distance


# Optimal Binary Search Tree
def optimal_bst(keys: List[int], freq: List[int]) -> int:
    n = len(keys)

    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    # One key
    for i in range(n):
        dp[i][i] = freq[i]

    # Increasing subtree length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            total_freq = sum(freq[i:j + 1])
            dp[i][j] = float('inf')

            for r in range(i, j + 1):

                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                cost = left + right + total_freq

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# Example: Floyd-Warshall

INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

print("Shortest Path Matrix:")

for row in result:
    print(row)


# Example: Optimal BST

keys = [10, 12, 20]
freq = [34, 8, 50]

cost = optimal_bst(keys, freq)

print("Optimal BST Cost:", cost)