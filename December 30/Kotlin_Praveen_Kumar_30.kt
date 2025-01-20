fun superEggDrop(k: Int, n: Int): Int {
    val dp = Array(k + 1) { IntArray(n + 1) }
    
    for (moves in 1..n) {
        for (eggs in 1..k) {
            dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1
            if (dp[eggs][moves] >= n) {
                return moves
            }
        }
    }
    return 0
}

fun main() {
    println(superEggDrop(2, 6))  // Output: 3
    println(superEggDrop(3, 14)) // Output: 4
}
