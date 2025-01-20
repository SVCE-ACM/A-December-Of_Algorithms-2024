fun alternatingSquareArrangement(R: Int, B: Int): String {
    if (kotlin.math.abs(R - B) > 1) {
        return "Not possible"
    }
    
    val result = StringBuilder()
    var (major, minor, majorColor, minorColor) = if (R >= B) {
        arrayOf(R, B, 'R', 'B')
    } else {
        arrayOf(B, R, 'B', 'R')
    }
    
    for (i in 0 until (major + minor)) {
        if (major > 0) {
            result.append(majorColor)
            major -= 1
        }
        if (minor > 0 && (result.isEmpty() || result.last() == majorColor)) {
            result.append(minorColor)
            minor -= 1
        }
    }
    
    return result.toString()
}
