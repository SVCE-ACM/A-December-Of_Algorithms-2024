fun canEscapeLava(nums: IntArray): Boolean {
    var maxReach = 0
    for (i in nums.indices) {
        if (i > maxReach) {
            return false
        }
        maxReach = maxOf(maxReach, i + nums[i])
        if (maxReach >= nums.size - 1) {
            return true
        }
    }
    return false
}

fun main() {
    val nums1 = intArrayOf(2, 3, 1, 0, 4)
    val nums2 = intArrayOf(3, 2, 1, 0, 4)
    println(canEscapeLava(nums1))  // Output: true
    println(canEscapeLava(nums2))  // Output: false
}
