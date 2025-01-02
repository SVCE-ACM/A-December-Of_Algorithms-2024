class Node(var data: Int) {
  var next: Node = _  // The next pointer of the node
}

object LinkedListIntersection {

  // Function to create a linked list from a list of values
  def createLinkedList(values: List[Int]): Node = {
    var head: Node = null
    for (value <- values) {
      val newNode = new Node(value)
      if (head == null) {
        head = newNode
      } else {
        var current = head
        while (current.next != null) {
          current = current.next
        }
        current.next = newNode
      }
    }
    head
  }

  // Function to find the intersection point between two linked lists
  def findIntersection(head1: Node, head2: Node, intersectionPos: Int): String = {
    if (intersectionPos == 0) {
      return "No intersection found."
    }

    var current1 = head1
    for (_ <- 1 until intersectionPos) {
      if (current1 == null) {
        return "Invalid intersection position"
      }
      current1 = current1.next
    }

    var current2 = head2
    while (current1 != null) {
      if (current1 == current2) {
        return current1.data.toString
      }
      current1 = current1.next
      current2 = current2.next
    }

    "No intersection found."
  }

  def main(args: Array[String]): Unit = {
    println("Enter the number of nodes in the first linked list:")
    val n1 = scala.io.StdIn.readInt()
    println("Enter the node values for the first list:")
    val values1 = scala.io.StdIn.readLine().split(" ").map(_.toInt).toList

    println("Enter the number of nodes in the second linked list:")
    val n2 = scala.io.StdIn.readInt()
    println("Enter the node values for the second list:")
    val values2 = scala.io.StdIn.readLine().split(" ").map(_.toInt).toList

    println("Enter the position of intersection:")
    val intersectionPos = scala.io.StdIn.readInt()

    val head1 = createLinkedList(values1)
    val head2 = createLinkedList(values2)

    val intersectionValue = findIntersection(head1, head2, intersectionPos)
    println(intersectionValue)
  }
}
