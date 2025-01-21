def minimum_swaps(arr):
    n = len(arr)
    
    arr_with_indices = []
    for i in range(n):
        arr_with_indices.append((arr[i], i))
    
    arr_with_indices.sort()
    
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or arr_with_indices[i][1] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_with_indices[j][1]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += (cycle_size - 1)
    
    return swaps

n = int(input("Enter the number of integers: "))
arr = list(map(int, input("Enter the integers separated by space: ").split()))
print("Minimum number of swaps required:", minimum_swaps(arr))
