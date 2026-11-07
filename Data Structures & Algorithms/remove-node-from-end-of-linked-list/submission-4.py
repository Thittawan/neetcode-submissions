# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head    
        if head.next == None and n > 0:
            return None
        while start != None:
            length += 1
            start = start.next
        start = head
        if n == length:
            return head.next
        while length != n+1 and start != None:
            start = start.next
            length -= 1
        temp = start.next
        if start.next != None:
            start.next = start.next.next # [1,2,3,4,5,6,7,8]
            temp.next = None
        else:
            start.next = None
        return head