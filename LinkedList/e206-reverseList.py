class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse(head):
    prev=None
    temp=head
    while temp != None:
        front=temp.next #Call this front and not next
        temp.next=prev
        prev=temp
        temp=front
    return prev #Just remember that there are 4 lines in the above loop
    # and remember to return prev and not temp

# Function to reverse a singly
# linked list using a recursion
"""
Memorize the notes below but remember the Intuition here is to pop off a stack in reverse order
Recursive calls give you the stack for free so no extra space needed
"""
def reverse2(head):
    if head.next is None:
        return head #Dont return nothing, return head, this is also crucial
    newHead= reverse2(head.next) #I missed head.next and this is crucial
    front=head.next #first remember this
    front.next=head #this is obvious
    head.next=None #Dont forget this, or error
    return newHead #Always return newHead



# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse2(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)