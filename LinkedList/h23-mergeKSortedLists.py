class Node:
    # Data stored in the node
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to insert node
def insert(root, item):
    temp = Node(item)

    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp

    return root

def toList(arr):
    root=None
    for num in arr:
        root=insert(root,num)
    return root

def toArray(head):
    res=[]
    while head is not None:
        res.append(head.data)
        head = head.next
    return res

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
    return result.next

def mergeKLists(lists):
    list1 = toList(lists[0])
    for i in range(1,len(lists)):
        list2=toList(lists[i])
        list1=mergeTwoLists(list1, list2)
    return toArray(list1)

print("Merged k sorted lists: ", end="")
print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))
