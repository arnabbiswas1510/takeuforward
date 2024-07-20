class Node:
    # Data stored in the node
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

def removeNthFromEnd(head, n):
    cnt=1
    prev=head
    head=head.next
    while head is not None:
        if cnt >= n+1:
            prev=prev.next
        cnt+=1
        head=head.next
    prev.next=prev.next.next

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

if __name__ == "__main__":
    # Example Linked Lists
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)
    list1.next.next.next = Node(4)
    list1.next.next.next.next = Node(5)
    n=2
    print("List with %dth node removed :" % (n))
    removeNthFromEnd(list1, n)
    print_linked_list(list1)