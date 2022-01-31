# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        traversal_list = []

        def preorder(root):
            if root==None:
                return 
            traversal_list.append(root.val)

            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return traversal_list


tree  = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(Solution().preorderTraversal(tree))