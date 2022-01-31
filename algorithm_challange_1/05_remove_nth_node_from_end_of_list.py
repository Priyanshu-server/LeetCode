# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) ->ListNode:
        first,last = (head,head)
        for _ in range(n):
            last = last.next
        
        if last == None:
            return head.next
        print("First pointer value : ",first.val)
        print("Last pointer value : ",last.val,"\n")

        while last.next:
            first = first.next
            last = last.next
        first.next = first.next.next

            
        
        return head

head = ListNode(1,None)
lst = head
for i in range(1,10):
    lst.next = ListNode()
    lst = lst.next
    lst.val = i+1
    

temp = head
while temp.next:
    print(temp.val,end = " ")
    temp = temp.next

print()
print(Solution().removeNthFromEnd(head,2))

