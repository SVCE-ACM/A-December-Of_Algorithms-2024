flag = True
arr = list(map(int,input().split()))
for i in range(len(arr) - 1):
    if(flag and arr[i] < arr[i+1]):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    elif(not flag and arr[i] > arr[i+1]):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    flag = not flag    
print(arr)        
