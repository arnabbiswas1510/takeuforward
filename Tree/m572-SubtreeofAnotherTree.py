"""
Naive approach, O(|s| * |t|)
For each node of s, let's check if it's subtree equals t. We can do that in a straightforward way by an isMatch function
: check if s and t match at the values of their roots, plus their subtrees match. Then, in our main function, we want to
check if s and t match, or if t is a subtree of a child of s.
"""
def isMatch(s,t):
    if not(s and t): #Returns True if either s or t is None
        return s is t #Means that s and t point to the same object (== in Java)
    return (s.val == t.val and
            isMatch(s.left, t.left) and
            isMatch(s.right, t.right))

def isSubtree(s,t):
    if isMatch(s,t):
        return True
    if not s:
        return False
    return isSubtree(s.left, t) or isSubtree(s.right, t)

"""
Advanced approach, O(|s| + |t|) (Merkle hashing):
For each node in a tree, we can create node.merkle, a hash representing it's subtree.
This hash is formed by hashing the concatenation of the merkle of the left child, the node's value, and the merkle of 
the right child. Then, two trees are identical if and only if the merkle hash of their roots are equal (except when 
there is a hash collision.) From there, finding the answer is straightforward: we simply check if any node in s has 
node.merkle == t.merkle
"""

def isSubtree2(self, s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()

    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle

    merkle(s)
    merkle(t)
    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or
                dfs(node.left) or dfs(node.right))
