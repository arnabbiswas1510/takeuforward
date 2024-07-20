"""
The evidence for this method is you assume fast is 1,2 and 3 nodes respectively behind slow and prove that they are
bound to catch up. Hint: 2 leads to 1 in next step and 3 leads to 2 in next step.
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def hasCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow == fast: #You cant do this before step 14 since then it will always return True based on lines 11,12
            return True
    return False

def beginCycle(head):
    if hasCycle(head):
        slow=head
        fast = head
        #First get to the meeting point as per above
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                break
        slow=head #Then take slow back to head
        #And keep cycling. Fast and Slow will meet at beginning of loop
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return slow.data
    return None


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if hasCycle(head):
        print("Loop detected in the linked list beginning at " + str(beginCycle(head)))
    else:
        print("No loop detected in the linked list.")