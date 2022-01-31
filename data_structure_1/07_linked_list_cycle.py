from collections import defaultdict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        i = 0
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False

    def pointer_slow_fast(self,head)->bool:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


lst1 = ListNode(3)
lst1.next = ListNode(2)
lst1.next.next = ListNode(0)
lst1.next.next.next = ListNode(-4)
lst1.next.next.next.next = lst1.next

def print_linked_list(node):
    while(node):
        print(node.val)
        node = node.next

# print_linked_list(lst1)
print(Solution().hasCycle(lst1))