def super_egg_drop(k: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for moves in range(1, n + 1):
        for eggs in range(1, k + 1):
            dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1
            if dp[eggs][moves] >= n:
                return moves

# Example test cases
print(super_egg_drop(2, 6))  # Output: 3
print(super_egg_drop(3, 14))  # Output: 4
