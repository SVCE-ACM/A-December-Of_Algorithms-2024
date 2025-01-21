def countWays(steps, distance):
    dp = [0] * (distance + 1)
    dp[0] = 1
    
    for i in range(1, distance + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
    
    return dp[distance]

steps = []
choice=1
while choice!=0:
    s = int(input("Enter steps:"))
    steps.append(s)
    choice=int(input("Do you want to enter more?(0/1):"))
distance = int(input("Enter distance:"))
print(countWays(steps, distance))  
