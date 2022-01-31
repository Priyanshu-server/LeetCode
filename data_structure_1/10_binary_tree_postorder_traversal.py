

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        traversal_list = []

        def postorder(root):
            if root==None:
                return 

            postorder(root.left)
            postorder(root.right)
            traversal_list.append(root.val)

        postorder(root)
        return traversal_list


tree  = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

print(Solution().postorderTraversal(tree))