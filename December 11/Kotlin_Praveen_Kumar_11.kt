fun robotReturnToOrigin(moves: String): Boolean {
    var x = 0
    var y = 0
    for (move in moves) {
        when (move) {
            'R' -> x++
            'L' -> x--
            'U' -> y++
            'D' -> y--
        }
    }
    return x == 0 && y == 0
}
