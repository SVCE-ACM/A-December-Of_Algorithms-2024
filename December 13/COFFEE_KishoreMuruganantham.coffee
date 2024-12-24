min_swaps = (nums) ->
  pos = {}
  for i, x in nums
    pos[x] = i

  sorted_nums = nums.sort()
  pos = {}
  for i, x in sorted_nums
    pos[x] = i

  count = 0
  for i, x in nums
    if pos[x] != i
      count += 1
      temp = nums[i]
      nums[i] = nums[pos[x]]
      nums[pos[x]] = temp
      pos[x] = i

  return count
