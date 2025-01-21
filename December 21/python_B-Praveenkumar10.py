class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def find_intersection(head1, head2):
    nodes_in_list1 = set()
    current1 = head1
    while current1:
        nodes_in_list1.add(current1)
        current1 = current1.next

    current2 = head2
    while current2:
        if current2 in nodes_in_list1:
            return f"The intersection point is: {current2.value}"
        current2 = current2.next

    return "No intersection found."

n = int(input("Enter the number of nodes in the first linked list: "))
values1 = list(map(int, input("Enter the node values: ").split()))
m = int(input("Enter the number of nodes in the second linked list: "))
values2 = list(map(int, input("Enter the node values: ").split()))
intersection_position = int(input("Enter the position of intersection: "))

head1 = create_linked_list(values1)
head2 = create_linked_list(values2)

if intersection_position > 0:
    intersect_node = head1
    for _ in range(intersection_position - 1):
        intersect_node = intersect_node.next

    tail2 = head2
    while tail2.next:
        tail2 = tail2.next
    tail2.next = intersect_node

result = find_intersection(head1, head2)
print(result)
