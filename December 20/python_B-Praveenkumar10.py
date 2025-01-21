def count_ways(steps, distance):
    dp = [0] * (distance + 1)
    dp[0] = 1
    for i in range(1, distance + 1):
        for step in steps:
            if i >= step:
                dp[i] += dp[i - step]
    return dp[distance]

steps = [1, 2, 3]
distance = 4
print(count_ways(steps, distance))
