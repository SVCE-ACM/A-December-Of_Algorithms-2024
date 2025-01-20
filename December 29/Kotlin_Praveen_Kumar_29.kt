import java.util.*

data class Portal(val x1: Int, val y1: Int, val x2: Int, val y2: Int, val w: Int)

fun minimumWeightPath(N: Int, M: Int, portals: List<Portal>): Int {
    val graph = mutableMapOf<Pair<Int, Int>, MutableList<Pair<Pair<Int, Int>, Int>>>()

    for (x1, y1, x2, y2, w in portals) {
        graph.getOrPut(Pair(x1, y1)) { mutableListOf() }.add(Pair(Pair(x2, y2), w))
        graph.getOrPut(Pair(x2, y2)) { mutableListOf() }.add(Pair(Pair(x1, y1), w))
    }

    val directions = listOf(Pair(0, 1), Pair(1, 0), Pair(0, -1), Pair(-1, 0))
    for (i in 1..N) {
        for (j in 1..M) {
            for ((di, dj) in directions) {
                val ni = i + di
                val nj = j + dj
                if (ni in 1..N && nj in 1..M) {
                    graph.getOrPut(Pair(i, j)) { mutableListOf() }.add(Pair(Pair(ni, nj), 0))
                }
            }
        }
    }

    val pq = PriorityQueue<Pair<Int, Pair<Int, Int>>>(compareBy { it.first })
    pq.add(Pair(0, Pair(1, 1)))

    val distances = mutableMapOf<Pair<Int, Int>, Int>().withDefault { Int.MAX_VALUE }
    distances[Pair(1, 1)] = 0

    while (pq.isNotEmpty()) {
        val (currentDist, currentNode) = pq.poll()

        if (currentNode == Pair(N, M)) {
            return currentDist
        }

        if (currentDist > distances.getValue(currentNode)) {
            continue
        }

        for ((neighbor, weight) in graph.getOrDefault(currentNode, emptyList())) {
            val distance = currentDist + weight
            if (distance < distances.getValue(neighbor)) {
                distances[neighbor] = distance
                pq.add(Pair(distance, neighbor))
            }
        }
    }

    return -1
}
