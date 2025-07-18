def maxDepth(root):
    if root is None:
        return 0
    return 1+max(maxDepth(root.left), maxDepth(root.right))

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([3,9,20,None,None,15,7])
print(maxDepth(r))