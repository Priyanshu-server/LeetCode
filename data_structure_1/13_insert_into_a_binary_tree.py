# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        temp = root
        if not temp: return TreeNode(val)
        while True:
            if temp.val < val:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TreeNode(val)
                    break
                
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TreeNode(val)
                    break
        return root





# Creation of Tree
tree  = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)

tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)

        
node = Solution().insertIntoBST(tree,5)




def levelOrder(root: TreeNode) -> list[int]:
    res = []
    q = deque()
    q.append(root)
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

print(levelOrder(node))