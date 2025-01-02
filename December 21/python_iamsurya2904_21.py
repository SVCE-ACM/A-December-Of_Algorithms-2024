class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def create_linked_list(values):
    head = None
    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
    return head

def find_intersection(head1, head2, intersection_pos):
    if intersection_pos == 0:
        return "No intersection found."

    current1 = head1
    for _ in range(intersection_pos - 1):
        if current1 is None:
            return "Invalid intersection position"
        current1 = current1.next

    current2 = head2
    while current1:
        if current1 == current2:
            return current1.data
        current1 = current1.next
        current2 = current2.next

    return "No intersection found."

n1 = int(input("Enter the number of nodes in the first linked list: "))
values1 = list(map(int, input("Enter the node values: ").split()))
n2 = int(input("Enter the number of nodes in the second linked list: "))
values2 = list(map(int, input("Enter the node values: ").split()))
intersection_pos = int(input("Enter the position of intersection: "))

head1 = create_linked_list(values1)
head2 = create_linked_list(values2)

intersection_value = find_intersection(head1, head2, intersection_pos)

print(intersection_value)

