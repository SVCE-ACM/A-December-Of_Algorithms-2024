def count_ways_to_reach_distance(steps, distance):
    dp = [0] * (distance + 1)
    
    dp[0] = 1
    
    for step in steps:
        for i in range(step, distance + 1):
            dp[i] += dp[i - step]
    
    return dp[distance]

steps = list(map(int, input("Enter the step sizes (space-separated): ").split()))
distance = int(input("Enter the target distance: "))

print(f"Number of ways to reach distance {distance}: {count_ways_to_reach_distance(steps, distance)}")
