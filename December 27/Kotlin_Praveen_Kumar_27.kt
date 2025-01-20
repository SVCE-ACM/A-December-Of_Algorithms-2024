fun trapRainWater(height: IntArray): Int {
    if (height.isEmpty()) {
        return 0
    }

    var left = 0
    var right = height.size - 1
    var leftMax = 0
    var rightMax = 0
    var trappedWater = 0

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left]
            } else {
                trappedWater += leftMax - height[left]
            }
            left++
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right]
            } else {
                trappedWater += rightMax - height[right]
            }
            right--
        }
    }

    return trappedWater
}

fun main() {
    val height1 = intArrayOf(0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)
    val height2 = intArrayOf(4, 2, 0, 3, 2, 5)
    println(trapRainWater(height1))  // Output: 6
    println(trapRainWater(height2))  // Output: 9
}
