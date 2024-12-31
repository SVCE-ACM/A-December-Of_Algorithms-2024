def countWays(steps, distance):
    dp = [0] * (distance + 1)
    dp[0] = 1
    for i in range(1, distance + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
    return dp[distance]

steps = set(map(int, input().split()))
distance = int(input())
print(countWays(steps, distance))
