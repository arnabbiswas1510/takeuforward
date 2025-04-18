"""
Key Insight:

In a BST, for any node n, if p and q are both less than n, then the LCA must be in the left subtree of n.

If p and q are both greater than n, then the LCA must be in the right subtree of n.

Otherwise, n is the LCA. This happens when:

One of p or q is equal to n (since a node is an ancestor of itself).

p is in the left subtree and q is in the right subtree (or vice versa), meaning n is the split point where p and q
diverge in different directions.

Brute force: Traverse in order and generate array and then compute common parent using n/2 formula
Optimal: Traverse in order and if direction needs to be changes to get to p and q then return that node. If
direction didnt need changing then return the node you encountered first as the LCA

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