class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val<list2.val:
            new_node = ListNode(list1.val)
            list1 = list1.next
        else:
            new_node = ListNode(list2.val)
            list2 = list2.next

        head = new_node
        
        while(list1 and list2):
            new_node.next = ListNode()
            new_node = new_node.next

            if list1.val < list2.val:
                new_node.val = list1.val
                list1 = list1.next
            else:
                new_node.val = list2.val
                list2 = list2.next
            

        new_node.next = list1 if list2 == None else list2
        
        return head


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


def traverse_linked_list(node):
    
    while(node):
        print(node.val)
        node = node.next

sol = Solution().mergeTwoLists(list1,list2)

traverse_linked_list(sol)