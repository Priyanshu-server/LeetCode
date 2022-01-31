# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        
        val1 = self.searchBST(root.left,val)
        val2 = self.searchBST(root.right,val)


        return val1 if val1 else val2



tree  = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)

tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)

        
node = Solution().searchBST(tree,2)
print(node.val)