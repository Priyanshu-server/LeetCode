
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l,r):
            if l and r:
                return l.val == r.val and dfs(l.left,r.right) and dfs(l.right,r.left)
            return l == r
        return dfs(root.left,root.right)

    def isSymmetricIteratively(self,root:TreeNode) ->bool:
        if not root:
            return True
        
        stack = [(root.left,root.right)]
        while stack:
            l,r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            
            stack.append((l.left,r.right))
            stack.append((l.right,r.left))
        
        return True


tree  = TreeNode(1)
tree.right = TreeNode(2)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

print(Solution().isSymmetric(tree))
print(Solution().isSymmetricIteratively(tree))