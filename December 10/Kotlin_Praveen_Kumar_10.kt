import java.util.*

fun findTaskOrder(tasks: List<Pair<String, List<String>>>): Any {
    val graph = mutableMapOf<String, MutableList<String>>()
    val inDegree = mutableMapOf<String, Int>()

    for ((task, dependencies) in tasks) {
        for (dependency in dependencies) {
            graph.putIfAbsent(dependency, mutableListOf())
            graph[dependency]?.add(task)
            inDegree[task] = inDegree.getOrDefault(task, 0) + 1
        }
    }

    val queue: Queue<String> = LinkedList(inDegree.filter { it.value == 0 }.keys)
    val result = mutableListOf<List<String>>()

    while (queue.isNotEmpty()) {
        val concurrentTasks = mutableListOf<String>()
        for (i in 0 until queue.size) {
            val task = queue.poll()
            concurrentTasks.add(task)
            graph[task]?.forEach { neighbor ->
                inDegree[neighbor] = inDegree[neighbor]!! - 1
                if (inDegree[neighbor] == 0) {
                    queue.add(neighbor)
                }
            }
        }
        result.add(concurrentTasks)
    }

    if (inDegree.values.any { it > 0 }) {
        return "Error: Cyclic dependency detected"
    }

    return result
}
