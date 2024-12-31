arr = list(map(int,input().split()))
target = int(input('Enter target :'))
result =[]
for i in arr:
    for j in arr:
        if i+j == target and (j,i) not in result:
            result.append((i,j))
print(result)            
