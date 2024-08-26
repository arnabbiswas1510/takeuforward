"""
Brute force: Traverse in order and generate array and then compute common parent using n/2 formula
Optimal: Traverse in order and if direction needs to be changes to get to p and q then return that node. If
direction didnt need changing then return the node you encountered first as the LCA

Intuition behind the below is here: https://github.com/arnabbiswas1510/takeuforward/blob/9f1b3c9139d8f9ae3398d4ed610993f18bf9d8d2/images/Tree/m235-LowestCommonAncestorOfBinarySearchTree.png
"""

def lowestCommonAncestor(root, p, q):
    if p < root.val and q <root.val:
        lowestCommonAncestor(root.left, p, q)
    elif p > root.val and q > root.val:
        lowestCommonAncestor(root.right, p, q)
    else:
        return root.val

#For the Iterative approach below you dont need Stack since there is no need to backtrack
def lowestCommonAncestor2(root, p, q):
    while root:
        if p < root.val and q <root.val:
            root = root.left
        elif p > root.val and q > root.val:
            root = root.right
        else:
            return root.val

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([6,2,8,0,4,7,9,None,None,3,5])
print(lowestCommonAncestor(r,2,8))