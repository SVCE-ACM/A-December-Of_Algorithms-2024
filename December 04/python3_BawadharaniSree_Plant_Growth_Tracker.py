def plant_growth_tracker(n):
    if n == 1 or n == 2:
        return 1
    prev1, prev2 = 1, 1
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
    return current
if __name__ == '__main__':
   n = int(input("Enter the number of months: "))
   result = plant_growth_tracker(n)
   print("Number of plants after", n, "months:", result)
