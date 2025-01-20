fun countCustomersWithOneReturn(returns: List<Int>): Int {
    return returns.count { it == 1 }
}
