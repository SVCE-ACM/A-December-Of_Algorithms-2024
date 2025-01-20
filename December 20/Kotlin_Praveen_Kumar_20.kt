fun countRobotPaths(steps: List<Int>, distance: Int): Int {
    if (distance == 0) {
        return 1
    }

    val dp = IntArray(distance + 1)
    dp[0] = 1

    for (i in 1..distance) {
        for (step in steps) {
            if (i - step >= 0) {
                dp[i] += dp[i - step]
            }
        }
    }

    return dp[distance]
}
