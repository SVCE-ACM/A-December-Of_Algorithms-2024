def plant_growth_tracker(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    prev, curr = 1, 1
    for i in range(3, n + 1):
        prev, curr = curr, prev + curr
        
    return curr

# Test cases
print(plant_growth_tracker(10))  # Output: 55
print(plant_growth_tracker(12))  # Output: 144

