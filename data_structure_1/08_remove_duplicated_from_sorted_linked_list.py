# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head


lst1 = ListNode(1)
lst1.next = ListNode(1)
lst1.next.next = ListNode(2)

node = Solution().deleteDuplicates(lst1)

def print_linked_list(node):
    while node:
        print(node.val)
        node = node.next

print_linked_list(node)