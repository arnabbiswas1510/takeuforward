def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return isSameTree(p.left, q.left) and p.val == q.val and isSameTree(p.right, q.right)

from treeOperations import Tree
t=Tree()
p=t.insertLevelOrder([1,2,1])
q=t.insertLevelOrder([1,1,2])
print(isSameTree(p,q))