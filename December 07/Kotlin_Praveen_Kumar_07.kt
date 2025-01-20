fun generatePascalTriangle(numRows: Int): List<List<Int>> {
    if (numRows == 0) {
        return emptyList()
    }

    val result = mutableListOf<List<Int>>()
    result.add(listOf(1))
    
    for (i in 1 until numRows) {
        val row = mutableListOf(1)
        for (j in 1 until i) {
            row.add(result[i - 1][j - 1] + result[i - 1][j])
        }
        row.add(1)
        result.add(row)
    }

    return result
}
