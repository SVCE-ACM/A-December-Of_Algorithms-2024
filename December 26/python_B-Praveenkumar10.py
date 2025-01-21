def can_reach_end(nums):
    max_reachable = 0
    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
    return max_reachable >= len(nums) - 1

nums1 = [2, 3, 1, 0, 4]
nums2 = [3, 2, 1, 0, 4]

print(can_reach_end(nums1))  
print(can_reach_end(nums2))  
