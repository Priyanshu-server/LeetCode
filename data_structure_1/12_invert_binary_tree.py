# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def dfs(node):
            if node:
                node.left,node.right = node.right,node.left
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return root



tree  = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)

tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)



# Traversing level order  <-->

def levelOrder(root: TreeNode) -> list[int]:
        res = []
        q = deque()
        q.append(root)

        # Here i will try to append the next layer nodes into the queue and popping the current layer
        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res

if __name__ == "__main__":
    print(levelOrder(tree))
    node = Solution().invertTree(tree)
    print(levelOrder(node))