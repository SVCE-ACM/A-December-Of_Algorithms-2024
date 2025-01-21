def superEggDrop(k, n):
    # Create a DP table where dp[i][j] represents the minimum moves for i eggs and j floors
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # Base cases: if we have only 1 egg, we need to do linear search (j drops for j floors)
    for j in range(n + 1):
        dp[1][j] = j
    
    # Fill the DP table for more than 1 egg
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            # Use binary search to minimize the worst case
            low, high = 1, j
            while low + 1 < high:
                mid = (low + high) // 2
                if dp[i - 1][mid - 1] < dp[i][j - mid]:
                    low = mid
                else:
                    high = mid
            dp[i][j] = 1 + min(max(dp[i - 1][low - 1], dp[i][j - low]), 
                               max(dp[i - 1][high - 1], dp[i][j - high]))
    
    return dp[k][n]

# Input
k = int(input("Enter the number of eggs: "))
n = int(input("Enter the number of floors: "))

# Output
print("Minimum moves required =", superEggDrop(k, n))
