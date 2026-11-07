# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        current = head
        nextt = head.next
        while current is not None:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt
        return prev