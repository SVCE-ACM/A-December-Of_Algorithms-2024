fun targetPairFinder(numbers: List<Int>, target: Int): List<Pair<Int, Int>> {
    val uniquePairs = mutableListOf<Pair<Int, Int>>()
    val seen = mutableSetOf<Int>()
    
    for (num in numbers) {
        val complement = target - num
        if (!seen.contains(complement)) {
            seen.add(num)
        } else {
            uniquePairs.add(Pair(complement, num))
        }
    }
    
    return uniquePairs
}
