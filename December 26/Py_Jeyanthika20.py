def can_escape_lava(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True
    return False

nums1 = [2, 3, 1, 0, 4]
nums2 = [3, 2, 1, 0, 4]
print(can_escape_lava(nums1))  
print(can_escape_lava(nums2))
