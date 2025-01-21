def min_moves_eggs_floors(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        dp[1][i] = i

    for eggs in range(2, k + 1):
        for floors in range(1, n + 1):
            low, high = 1, floors
            while low + 1 < high:
                mid = (low + high) // 2
                break_case = dp[eggs - 1][mid - 1]
                no_break_case = dp[eggs][floors - mid]

                if break_case > no_break_case:
                    high = mid
                else:
                    low = mid

            dp[eggs][floors] = 1 + min(
                max(dp[eggs - 1][low - 1], dp[eggs][floors - low]),
                max(dp[eggs - 1][high - 1], dp[eggs][floors - high])
            )

    return dp[k][n]

print(min_moves_eggs_floors(2, 6)) 
print(min_moves_eggs_floors(3, 14)) 
