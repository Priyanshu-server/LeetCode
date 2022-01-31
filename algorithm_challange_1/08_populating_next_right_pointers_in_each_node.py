class Node:
    def __init__(self, val: int = 0, left =  None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):

        black = root
        while(black != None and black.left != None):
            n = black

            while True:
                n.left.next = n.right
                if n.next == None: break
                n.right.next = n.next.left
                n = n.next
            black = black.left
        return root



node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)

        
sol_node = Solution().connect(node)
print(node)