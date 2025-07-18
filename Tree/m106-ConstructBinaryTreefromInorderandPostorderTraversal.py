"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is
the postorder traversal of the same tree, construct and return the binary tree.

Remember the method definitions and that you need an external hashMap
"""
from treeOperations import Node, Tree

def buildTree(inorder, postorder):
    def helper(inLeft, inRight):
        #Dont forget terminal condition
        if not postorder or inLeft > inRight:
            return None
        val = postorder.pop()
        root=Node(val)
        index=inMap[val] #Required to do this in this step
        # If done in the 2 lines below will cause bug since its in recursive context
        root.left=helper(inLeft,index-1) #Remember to use inLeft and inRight here as terminal indexes and not 0, len
        root.right=helper(index+1,inRight)
        return root
    #Note that it's a map of val:idx
    inMap={val:idx for idx, val in enumerate(inorder)}
    return helper(0,len(inorder))

t=Tree()
t.printLevelOrder(buildTree([9,3,15,20,7], [9,15,7,20,3]))