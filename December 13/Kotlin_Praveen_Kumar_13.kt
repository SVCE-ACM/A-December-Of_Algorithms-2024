fun minSwaps(nums: IntArray): Int {
    val pos = nums.sorted().withIndex().associate { it.value to it.index }
    var count = 0
    for (i in nums.indices) {
        if (pos[nums[i]] != i) {
            count++
            val temp = nums[i]
            nums[i] = nums[pos[nums[i]]!!]
            nums[pos[nums[i]]!!] = temp
            pos[nums[i]] = i
        }
    }
    return count
}
