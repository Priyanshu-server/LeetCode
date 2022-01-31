# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head:ListNode, val: int) ->ListNode:

        while head and head.val == val:
            head = head.next

        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head


lst1 = ListNode(1)
lst1.next = ListNode(2)
lst1.next.next = ListNode(6)
lst1.next.next.next = ListNode(3)
lst1.next.next.next.next = ListNode(4)
lst1.next.next.next.next.next = ListNode(5)
lst1.next.next.next.next.next.next = ListNode(6)

def print_linked_list(node):
    while node:
        print(node.val)
        node = node.next

node = Solution().removeElements(lst1,6)
print_linked_list(node)