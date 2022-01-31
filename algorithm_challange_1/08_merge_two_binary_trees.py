class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
            if root1 == None and root2 == None:
                return 
            
            v1 = root1.val if root1 else 0
            v2 = root2.val if root2 else 0

            new_node = TreeNode(v1+v2)
            root1_left = root1.left if root1 else None
            root2_left = root2.left if root2 else None

            new_node.left = self.mergeTrees(root1_left,root2_left)

            root1_right = root1.right if root1 else None
            root2_right = root2.right if root2 else None

            new_node.right = self.mergeTrees(root1_right,root2_right)

            return new_node


# Root 1 Creation
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
# Root 2 Creation
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

# Traversing Node Function
def traversing__node(node):
    if node==None:
        return 
    traversing__node(node.left)
    print(node.val)
    traversing__node(node.right)

# Executing Solution
new_node = Solution().mergeTrees(root1,root2)
traversing__node(new_node)
