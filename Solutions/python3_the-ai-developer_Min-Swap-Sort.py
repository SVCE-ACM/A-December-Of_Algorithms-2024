def MinSwaps2Sort(arr):
    n = len(arr)
    paired = [(arr[i], i) for i in range(n)]
    paired.sort(key=lambda x: x[0])

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or paired[i][1] == i:
            continue
        
        cycle_length = 0
        current = i
        while not visited[current]:
            visited[current] = True
            next_index = paired[current][1]  
            current = next_index
            cycle_length += 1
        
        if cycle_length > 1:
            swaps += (cycle_length - 1)

    return swaps

print(f"Min No.Of Swaps: {MinSwaps2Sort(list(map(int,input('Enter Graph List: ').split(' '))))}")

