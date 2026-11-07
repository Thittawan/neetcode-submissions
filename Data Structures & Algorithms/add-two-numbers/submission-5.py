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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        temp1 = current1
        temp2 = current2
        prev = None
        while temp1 or temp2:
            val1 = 0
            val2 = 0
            if temp1:
                val1 = temp1.val
            if temp2:
                val2 = temp2.val
            val = val1 + val2
            string_val = str(val)
            if not temp1:
                prev.next = current2
                temp1 = current2
                temp1.val = 0
                current2.next = None                 

            if len(string_val) > 1:
                temp1.val = int(string_val[1])
                if temp1.next:
                    temp1.next.val = temp1.next.val + int(string_val[0])
                else:
                    temp1.next = ListNode(int(string_val[0]))
            else:
                temp1.val = val
            
            if temp1: 
                prev = temp1
                temp1 = temp1.next
            if temp2: temp2 = temp2.next
        return current1
        