def canJump(nums):
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:
            return False
        
        farthest = max(farthest, i + nums[i])
        
        if farthest >= len(nums) - 1:
            return True
    
    return False

nums = list(map(int, input("Enter the list of numbers: ").split()))
print(canJump(nums))
