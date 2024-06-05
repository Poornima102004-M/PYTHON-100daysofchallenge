def tsp(distance_matrix):
    n = len(distance_matrix)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) == 0:
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + distance_matrix[u][v])

    return min(dp[(1 << n) - 1][v] + distance_matrix[v][0] for v in range(1, n))

# Example usage
distance_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]
tsp(distance_matrix)
