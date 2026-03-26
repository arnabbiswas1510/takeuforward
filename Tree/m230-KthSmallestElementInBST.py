"""
Brute force is to do an in order traversal and store the elements in an array. This array will be sorted and return kth
element. n time but n space.
Optimal solution is to perform in order traversal and keep reducing the cnt and return element when count is 0
"""
#In recursive calls in order to save state pass all variables in a collection instead of by value.
# See below line 38 also for how this is done. No need to do this if the value wont change, but in case of cnt (like
# this), this is required to do
def kthSmallest(root, k):
    if root.left:
        kthSmallest(root.left, k)
    k[0]-=1
    if k[0]==0:
        k.append(root.val)
        return
    if root.right:
        kthSmallest(root.right, k)


#Iterative, always use stack since recursive calls
def kthSmallest2(root, k):
    stack=[]
    cnt=0
    cur=root #Dont really need this
    while cur or stack: #Or is critical here, not and
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        cnt+=1
        if cnt==k:
            return cur.val
        cur=cur.right
    return -1

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([5,3,6,2,4,None,None,1])
k=[3]
kthSmallest(r, k)
print(k[1])
