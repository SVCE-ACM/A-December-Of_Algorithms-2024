class Node(val data: Int) {
    var next: Node? = null
}

fun createLinkedList(values: List<Int>): Node? {
    var head: Node? = null
    for (value in values) {
        val newNode = Node(value)
        if (head == null) {
            head = newNode
        } else {
            var current = head
            while (current?.next != null) {
                current = current.next
            }
            current?.next = newNode
        }
    }
    return head
}

fun findIntersection(head1: Node?, head2: Node?, intersectionPos: Int): String {
    if (intersectionPos == 0) {
        return "No intersection found."
    }

    var current1 = head1
    for (i in 1 until intersectionPos) {
        if (current1 == null) {
            return "Invalid intersection position"
        }
        current1 = current1.next
    }

    var current2 = head2
    while (current1 != null) {
        if (current1 == current2) {
            return current1.data.toString()
        }
        current1 = current1.next
        current2 = current2?.next
    }

    return "No intersection found."
}

fun main() {
    val n1 = readLine()!!.toInt()
    val values1 = readLine()!!.split(" ").map { it.toInt() }
    val n2 = readLine()!!.toInt()
    val values2 = readLine()!!.split(" ").map { it.toInt() }
    val intersectionPos = readLine()!!.toInt()

    val head1 = createLinkedList(values1)
    val head2 = createLinkedList(values2)

    val intersectionValue = findIntersection(head1, head2, intersectionPos)

    println(intersectionValue)
}
