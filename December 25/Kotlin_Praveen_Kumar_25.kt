import java.io.File
import java.io.ObjectInputStream
import java.io.ObjectOutputStream
import java.util.PriorityQueue

data class Task(val description: String, val priority: Int)

class TaskScheduler(private val filename: String = "tasks.ser") {
    private val heap: PriorityQueue<Task> = PriorityQueue { t1, t2 -> t2.priority - t1.priority }
    private val taskMap: MutableMap<String, Task> = mutableMapOf()

    init {
        loadTasks()
    }

    fun addTask(description: String, priority: Int) {
        if (taskMap.contains(description)) {
            println("Task '$description' already exists.")
            return
        }
        val task = Task(description, priority)
        heap.add(task)
        taskMap[description] = task
        saveTasks()
    }

    fun removeTask(description: String) {
        val task = taskMap[description] ?: run {
            println("Task '$description' not found.")
            return
        }
        heap.remove(task)
        taskMap.remove(description)
        saveTasks()
    }

    fun searchTask(description: String): Task? {
        return taskMap[description]
    }

    fun displayTasks(): List<Pair<String, Int>> {
        return heap.sortedByDescending { it.priority }.map { it.description to it.priority }
    }

    private fun saveTasks() {
        ObjectOutputStream(File(filename).outputStream()).use { it.writeObject(Pair(heap, taskMap)) }
    }

    private fun loadTasks() {
        if (File(filename).exists()) {
            ObjectInputStream(File(filename).inputStream()).use { 
                val (loadedHeap, loadedMap) = it.readObject() as Pair<PriorityQueue<Task>, MutableMap<String, Task>>
                heap.addAll(loadedHeap)
                taskMap.putAll(loadedMap)
            }
        }
    }
}

// Example usage
fun main() {
    val scheduler = TaskScheduler()
    scheduler.addTask("Complete Assignment", 2)
    scheduler.addTask("Buy Groceries", 1)
    println("Tasks: ${scheduler.displayTasks()}")
    scheduler.removeTask("Complete Assignment")
    println("Tasks after removal: ${scheduler.displayTasks()}")
}
