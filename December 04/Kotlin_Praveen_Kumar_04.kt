fun plantGrowthTracker(n: Int): Int {
    if (n == 1 || n == 2) return 1

    var prev = 1
    var curr = 1
    for (i in 3..n) {
        val temp = curr
        curr += prev
        prev = temp
    }

    return curr
}
