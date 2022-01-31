# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and  head.val == head.next.val:
                   head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
                
        return dummy.next



# Nodes
list_values = [1,2,3,3,4,4,5]
list_values = [1,1,1,2,3]
node = ListNode(list_values[0])
head = node
for val in list_values[1:]:
    node.next  = ListNode()
    node = node.next
    node.val = val


# Traversing thorughout the node
def traverse(head):
    res = []
    while head:
        res += [head.val]
        head = head.next
    return res

print(traverse(head))

head_node = Solution().deleteDuplicates(head)
print(traverse(head_node))