fun josephus(n: Int, k: Int): Int {
    var safePosition = 0
    for (i in 1..n) {
        safePosition = (safePosition + k) % i
    }
    return safePosition + 1
}
