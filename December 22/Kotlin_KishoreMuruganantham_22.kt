import kotlin.math.sqrt

fun earthquakePropagation(buildings: List<List<Int>>): Int {
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
                    affected += 1
                }
            }
        }
        maxAffected = maxOf(maxAffected, affected)
    }

    return maxAffected
}

fun main() {
    val buildings = listOf(
        listOf(2, 1, 3),
        listOf(6, 1, 4)
    )
    val maxAffected = earthquakePropagation(buildings)
    println(maxAffected)
}
