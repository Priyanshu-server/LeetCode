# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        val_set = set()
        nodes = [root]

        while nodes:
            node = nodes.pop(0)
            if k-node.val in val_set: return True
            val_set.add(node.val)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
        return False



tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right  =TreeNode(6)
tree.left.left  = TreeNode(2)
tree.left.right = TreeNode(4)

tree.right.right = TreeNode(7)

print(Solution().findTarget(tree,9))