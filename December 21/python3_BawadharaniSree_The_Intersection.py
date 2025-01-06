class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def find_intersection_point(head1, head2):
    p1 = head1
    p2 = head2
    
    while p1 != p2:
        p1 = p1.next if p1 else head2  
        p2 = p2.next if p2 else head1  

    return p1

N = int(input("Enter the number of nodes in the first linked list: "))
list1_values = list(map(int, input("Enter the node values: ").split()))
M = int(input("Enter the number of nodes in the second linked list: "))
list2_values = list(map(int, input("Enter the node values: ").split()))
intersection_position = int(input("Enter the position of intersection: "))

list1_head = create_linked_list(list1_values)
list2_head = create_linked_list(list2_values)

if intersection_position > 0:
    intersection_node = list1_head
    for _ in range(intersection_position - 1):
        intersection_node = intersection_node.next
    
    last_node = list2_head
    while last_node.next:
        last_node = last_node.next
    last_node.next = intersection_node

intersection = find_intersection_point(list1_head, list2_head)

if intersection:
    print(f"The intersection point is: {intersection.val}")
else:
    print("No intersection found.")
