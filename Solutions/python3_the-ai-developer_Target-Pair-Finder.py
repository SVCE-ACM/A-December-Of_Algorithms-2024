IntList=list(map(int,input("Enter List Of Integers: ").split(" ")))
Trgt=int(input("Enter Target Sum: "))
def twoSum(nums, target):
    Res=[]
    n = len(nums)
    for i in range(n - 1):
        for j in range(i,n):
            if nums[i] + nums[j] == target:
                Res.append([nums[i],nums[j]])
    return Res

print(f"Solution Arr: {twoSum(IntList,Trgt)}")
