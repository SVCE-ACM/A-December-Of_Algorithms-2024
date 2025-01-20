fun fastInverseSqrt(x: Double): Double {
    val threeHalfs = 1.5
    val x2 = x * 0.5
    var i = java.lang.Double.doubleToRawLongBits(x)
    i = 0x5f3759df - (i shr 1)
    var y = java.lang.Double.longBitsToDouble(i)
    y = y * (threeHalfs - (x2 * y * y))
    return y
}

fun normalizeVectors(vectors: List<Triple<Double, Double, Double>>): List<Triple<Double, Double, Double>> {
    val result = mutableListOf<Triple<Double, Double, Double>>()
    for (vec in vectors) {
        val (x, y, z) = vec
        val magnitudeSquared = x * x + y * y + z * z
        val invMagnitude = fastInverseSqrt(magnitudeSquared)
        result.add(Triple(x * invMagnitude, y * invMagnitude, z * invMagnitude))
    }
    return result
}

fun main() {
    val vectors = listOf(
        Triple(3.0, 4.0, 0.0),
        Triple(-6.0, 8.0, 0.0),
        Triple(5.0, 12.0, 0.0)
    )

    val normalizedVectors = normalizeVectors(vectors)
    for (vec in normalizedVectors) {
        println("${"%.6f".format(vec.first)} ${"%.6f".format(vec.second)} ${"%.6f".format(vec.third)}")
    }
}
