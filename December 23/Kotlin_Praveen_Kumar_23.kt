fun crystalGridFinalResult(grid: Array<IntArray>): Int {
    val n = grid.size
    var primarySum = 0
    var secondarySum = 0
    var boundarySum = 0

    for (i in 0 until n) {
        primarySum += grid[i][i]
        secondarySum += grid[i][n - 1 - i]
        for (j in 0 until n) {
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
                boundarySum += grid[i][j]
            }
        }
    }

    val diagonalEnergy = Math.abs(primarySum - secondarySum)
    return diagonalEnergy + boundarySum
}

fun main() {
    val grid = arrayOf(
        intArrayOf(1, 2, 3),
        intArrayOf(4, 5, 6),
        intArrayOf(7, 8, 9)
    )
    println(crystalGridFinalResult(grid))  // Output: 40
}
