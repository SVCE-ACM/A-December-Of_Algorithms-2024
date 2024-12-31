class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findIntersection(head1, head2, pos):
    if pos == 0:
        return "No intersection found."
    
    curr1 = head1
    curr2 = head2
    for _ in range(pos - 1):
        if curr1 is not None:
            curr1 = curr1.next
    if curr1 is not None:
        intersection_node = curr1
        while curr1.next is not None:
            curr1 = curr1.next
        curr1.next = head2
        while head1 is not None and head2 is not None:
            if head1 == head2:
                return f"The intersection point is: {head1.val}"
            head1 = head1.next
            head2 = head2.next
        return "No intersection found."
    else:
        return "No intersection found."

def createLinkedList(arr):
    head = ListNode(arr[0])
    temp = head
    for val in arr[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head
n1 = int(input("Enter the number of nodes in the first linked list: "))
list1 = list(map(int, input("Enter the node values: ").split()))
n2 = int(input("Enter the number of nodes in the second linked list: "))
list2 = list(map(int, input("Enter the node values: ").split()))
pos = int(input("Enter the position of intersection: "))

head1 = createLinkedList(list1)
head2 = createLinkedList(list2)

print(findIntersection(head1, head2, pos))
