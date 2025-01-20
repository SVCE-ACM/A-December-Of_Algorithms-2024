fun findMissingNumber(N: Int, array: IntArray): Int {
    val expectedSum = N * (N + 1) / 2
    val actualSum = array.sum()
    return expectedSum - actualSum
}
