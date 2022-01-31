# Definition for a binary tree node.
from platform import node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root,p,q):
        cur = root

        while cur:
            if p.val > cur.val and q.val>cur.val:
                cur = cur.right
            elif p.val<cur.val and q.val<cur.val:
                cur = cur.left

            # this 'else' will executed when p is in left and q in in right or vice-versa and also
            # if curr value if either p or q because Upper conditions will not satisfied by it !
            else: 
                return cur


tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)

tree.right.left  = TreeNode(7)
tree.right.right  = TreeNode(9)


print(Solution().lowestCommonAncestor(tree,tree.left,tree.right).val)