"""
Simple BFS traversal using a queue
"""

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([3,9,20,None,None,15,7])
t.printLevelOrder(r)