def trap_rain_water(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # Compute left max heights
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Compute right max heights
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - height[i]

    return trapped_water

# Get input from the user
def main():
    print("Trapping Rain Water Problem")
    height = list(map(int, input("Enter the bar heights separated by spaces: ").split()))
    result = trap_rain_water(height)
    print(f"Total trapped rain water: {result}")

if __name__ == "__main__":
    main()

