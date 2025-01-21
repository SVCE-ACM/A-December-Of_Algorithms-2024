def trap_water(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n
    trapped_water = 0

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]

print(trap_water(height1)) 
print(trap_water(height2))
