import kotlin.math.sqrt

fun earthquakePropagation(buildings: Array<IntArray>): Int {
    var maxAffected = 0

    for (i in buildings.indices) {
        var affected = 1
        for (j in buildings.indices) {
            if (i != j) {
                val distance = sqrt(
                    ((buildings[i][0] - buildings[j][0]).toDouble()).pow(2.0) + 
                    ((buildings[i][1] - buildings[j][1]).toDouble()).pow(2.0)
                )
                if (distance <= buildings[i][2].toDouble()) {
                    affected++
                }
            }
        }
        maxAffected = maxOf(maxAffected, affected)
    }

    return maxAffected
}

fun main() {
    val buildings = arrayOf(intArrayOf(2, 1, 3), intArrayOf(6, 1, 4))
    val maxAffected = earthquakePropagation(buildings)
    println(maxAffected)
}
