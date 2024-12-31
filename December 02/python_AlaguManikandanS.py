def wave_sort(arr):
    n = len(arr)
    arr.sort()
    
    for i in range(0, n, 2):
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        
        if i + 1 < n and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

arr = [5,4,6,2,3,7,9,8,1]
wave_sorted_arr = wave_sort(arr)
print(wave_sorted_arr)  
