class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1




tree  = TreeNode(3)
tree.right = TreeNode(20)
tree.left = TreeNode(9)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().maxDepth(tree))  