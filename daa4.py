def knapsack_dp(W, wt, val, n):
    # Initialize a 2D array to store the maximum profit for each subproblem
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build the table K[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0  # Base case: zero items or zero capacity
            elif wt[i - 1] <= w:
                # Include the item or exclude it, choose the maximum profit
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                # If item cannot be included, carry forward the maximum value so far
                K[i][w] = K[i - 1][w]

    # The maximum profit for the full capacity and all items
    max_profit = K[n][W]

    # Backtracking to find the items included in the knapsack
    w = W
    selected_items = [0] * n  # Initialize selection list with 0's
    for i in range(n, 0, -1):
        if max_profit <= 0:
            break
        # Check if this item was included in the optimal solution
        if max_profit != K[i - 1][w]:
            selected_items[i - 1] = 1  # Mark this item as included
            max_profit -= val[i - 1]   # Subtract its value from max_profit
            w -= wt[i - 1]             # Reduce remaining weight

    return K[n][W], selected_items  # Return maximum profit and selection list


# Example usage
print("Enter number of items:")
n = int(input())

print("Enter weights of items:")
wt = list(map(int, input().split()))

print("Enter values of items:")
val = list(map(int, input().split()))

print("Enter maximum capacity of knapsack:")
W = int(input())

# Calculate the maximum profit and the selection list
max_profit, selected_items = knapsack_dp(W, wt, val, n)

# Print results
print("Maximum possible profit =", max_profit)
print("Items selected (0-based index):", selected_items)
