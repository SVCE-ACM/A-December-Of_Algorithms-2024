def count_robot_paths(steps, distance):
    if distance == 0:
        return 1

    dp = [0] * (distance + 1)
    dp[0] = 1

    for i in range(1, distance + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]

    return dp[distance]

