def plant_growth(n):
    if n == 1 or n == 2:
        return 1
    prev1 = 1
    prev2 = 1 
    for month in range(3, n + 1):
        current = prev1 + prev2  
        prev1 = prev2  
        prev2 = current  
    return prev2

n = int(input("No of Months: "))
print(plant_growth(n))
