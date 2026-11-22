from typing import List


# 2D Dynamic Programming
def knapsack_01_2d(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# 1D Dynamic Programming
def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    return dp[capacity]


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum value using 2D DP:",
      knapsack_01_2d(weights, values, capacity))

print("Maximum value using 1D DP:",
      knapsack_01(weights, values, capacity))