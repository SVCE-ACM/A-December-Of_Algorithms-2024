def eggDrop(k, n):
    dp = [[0 for x in range(n + 1)] for y in range(k + 1)]
    
    for i in range(n + 1):
        dp[1][i] = i
    
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                dp[i][j] = min(dp[i][j], res)
    
    return dp[k][n]

k, n = map(int, input("Enter number of eggs (k) and number of floors (n): ").split())
print(f"Minimum moves required with {k} eggs and {n} floors: {eggDrop(k, n)}")
