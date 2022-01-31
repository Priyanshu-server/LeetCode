class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head

        
        new_node = self.reverseListRecursive(head.next)

        head.next.next = head
        head.next = None

        return new_node
    


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)


def traverse_linked_list(node):
    print("Reversed Linked List : ", end = " ")
    while(node):
        print(node.val,end = " ")
        node = node.next
    print()



# sol = Solution().reverseList(list1)
# traverse_linked_list(sol)

sol2 = Solution().reverseList(list1)
traverse_linked_list(sol2)

