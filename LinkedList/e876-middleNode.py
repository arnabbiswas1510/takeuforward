class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.data

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(get_middle(head))