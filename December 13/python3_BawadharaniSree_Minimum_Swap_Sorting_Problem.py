def minimum_swaps_to_sort(arr):
    n = len(arr)
    visited = [False] * n
    arr_with_indices = list(enumerate(arr))
    arr_with_indices.sort(key=lambda x: x[1])
    swaps = 0

    for i in range(n):
        if visited[i] or arr_with_indices[i][0] == i:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_with_indices[j][0]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps


N = int(input("Enter the number of integers: "))
arr = list(map(int, input("Enter the integers separated by spaces: ").split()))


result = minimum_swaps_to_sort(arr)
print(result)