def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
# weights = [2,5,1]
# values = [10,20,5]
capacity = 10
max_value, selected_items = knapsack(weights, values, capacity)
print(f"Maximum value achievable: {max_value}")
print(f"Selected items: {selected_items}")
