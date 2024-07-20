class Node:
    # Data stored in the node
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to merge two sorted linked lists
def mergeTwoLists(list1, list2):
    result=Node(-1) #You need to initialize new list this way
    temp=result
    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            temp.next = list1 #Do this instead of temp.data=list1.data
            list1=list1.next
        else:
            temp.next = list2
            list2=list2.next
        temp=temp.next
    if list1 is not None:
        temp.next=list1
    if list2 is not None:
        temp.next=list2
    return result


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
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    print("First sorted linked list: ", end="")
    print_linked_list(list1)

    print("Second sorted linked list: ", end="")
    print_linked_list(list2)

    merged_list = mergeTwoLists(list1, list2)

    print("Merged sorted linked list: ", end="")
    print_linked_list(merged_list)