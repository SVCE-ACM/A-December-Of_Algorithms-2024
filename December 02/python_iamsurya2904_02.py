def wave_sort(arr):
    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Test cases
print(wave_sort([10, 5, 6, 3, 2, 20, 100, 80]))  # Output: [10, 5, 6, 2, 20, 3, 100, 80]
print(wave_sort([1, 2, 3, 4, 5, 6]))            # Output: [2, 1, 4, 3, 6, 5]

