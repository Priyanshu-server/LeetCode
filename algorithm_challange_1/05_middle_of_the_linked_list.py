# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.val


head = ListNode()
lst = head
for i in range(10):
    lst.val = i+1
    lst.next = ListNode()
    lst = lst.next

temp = head
while temp.next:
    print(temp.val,end = " ")
    temp = temp.next

print()
print(Solution().middleNode(head))

