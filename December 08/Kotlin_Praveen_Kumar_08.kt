fun digitSquareSum(N: Int): Int {
    fun digitSquareSumOfNumber(num: Int): Int {
        var total = 0
        var number = num
        while (number > 0) {
            val digit = number % 10
            total += digit * digit
            number /= 10
        }
        return total
    }

    var totalSum = 0
    for (i in 1..N) {
        totalSum += digitSquareSumOfNumber(i)
    }
    return totalSum
}
