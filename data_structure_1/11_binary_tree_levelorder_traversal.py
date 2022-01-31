from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
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


tree  = TreeNode(3)
tree.right = TreeNode(20)
tree.left = TreeNode(9)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().levelOrder(tree))  