
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: 
            return False
        if (not root.left) and (not root.right):
            if targetSum - root.val == 0:
                return True
            else:
                return False

        result1,result2 = 0,0
        
        if root.left:
            result1 = self.hasPathSum(root.left,targetSum - root.val)
        if root.right:
            result2 = self.hasPathSum(root.right,targetSum - root.val)

        return result1 or result2

# Creating Tree
tree  = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)

tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)

tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)


tree2 = TreeNode(-2)
tree2.right = TreeNode(-3)
# Solution
print(Solution().hasPathSum(tree,22))
print(Solution().hasPathSum(tree2,-5))