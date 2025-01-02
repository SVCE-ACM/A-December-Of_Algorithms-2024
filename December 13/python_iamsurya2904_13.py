def min_swaps(nums):
    pos = {x: i for i, x in enumerate(sorted(nums))}
    count = 0
    for i, x in enumerate(nums):
        if pos[x] != i:
            count += 1
            temp = nums[i]
            nums[i] = nums[pos[x]]
            nums[pos[x]] = temp
            pos[x] = i
    return count
