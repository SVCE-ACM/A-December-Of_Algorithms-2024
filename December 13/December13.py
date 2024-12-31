n = int(input())
nums = list(map(int, input().split()))
cost = 0
for i in range(n):
    index = i
    for j in range(i+1,n):
        if(nums[j]<nums[index]):
            index = j
    if(index!=i):
        nums[i], nums[index] = nums[index], nums[i]
        cost+=1
print(cost)