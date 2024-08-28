"""
In order to deserialize a tree from an Array you need more than one traversals of that tree. One of the traversals need
to be Inorder. The other traversal can be pre or postorder but inorder is must as one of the traversals

Instead: Do level order traversal (BFS) to generate an array. Then deserialize the three from the array using the formula:
L=2n+1, R=2n+2
"""

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,6,7,3,4,5])
t.printLevelOrder(r)