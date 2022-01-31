class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        traversal_list = []

        def inorder(root):
            if root==None:
                return 

            inorder(root.left)
            traversal_list.append(root.val)
            inorder(root.right)

        inorder(root)
        return traversal_list


tree  = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(Solution().inorderTraversal(tree))