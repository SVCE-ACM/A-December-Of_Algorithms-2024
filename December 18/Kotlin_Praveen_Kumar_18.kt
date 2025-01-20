fun gemValue(gem: Char): Int {
    return when (gem) {
        'D' -> 500
        'R' -> 250
        'E' -> 100
        else -> 0
    }
}

fun maxPalindromicChainProfit(chain: String): Int {
    val n = chain.length
    if (n == 0) return 0

    val s = "@#" + chain.map { "#$it" }.joinToString("") + "#$"
    val p = IntArray(s.length)
    var c = 0
    var r = 0

    for (i in 1 until s.length - 1) {
        if (i < r) {
            p[i] = minOf(r - i, p[2 * c - i])
        }
        while (i + p[i] + 1 < s.length && s[i + p[i] + 1] == s[i - p[i] - 1]) {
            p[i]++
        }
        if (i + p[i] > r) {
            c = i
            r = i + p[i]
        }
    }

    var maxLength = 0
    var center = 0
    for (i in 1 until s.length - 1) {
        if (p[i] > maxLength) {
            maxLength = p[i]
            center = i
        }
    }

    val start = (center - maxLength) / 2
    val end = (center + maxLength) / 2
