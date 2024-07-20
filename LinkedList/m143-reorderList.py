class Node:
    # Data stored in the node
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

def halveList(head):
    slow=head
    fast=head
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next
    return slow

def reverse(head):
    prev=None
    temp=head
    while temp != None:
        front=temp.next #Call this front and not next
        temp.next=prev
        prev=temp
        temp=front
    return prev

def reorderList(head):
    secondHalf=halveList(head)
    secondHalf=reverse(secondHalf)
    reordered=Node(-1)
    temp=reordered
    flag=True
    while head is not None and secondHalf is not None:
        if flag:
            temp.next=head
            head=head.next
            flag=False
        else:
            temp.next=secondHalf
            secondHalf=secondHalf.next
            flag=True
        temp=temp.next
    return reordered.next

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
    reordered=reorderList(list1)
    print("Reordered list : ")
    print_linked_list(reordered)