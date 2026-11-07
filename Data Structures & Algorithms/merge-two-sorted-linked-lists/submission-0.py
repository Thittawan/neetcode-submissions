# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1 = list1
        start2 = list2
        result = None

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if start1.val < start2.val:
            result = start1
            start1 = start1.next
        else:
            result = start2
            start2 = start2.next

        temp = result

        while start1 is not None and start2 is not None:
            print(start1.val)
            print(start2.val)
            if start1.val < start2.val:
                temp.next = start1
                start1 = start1.next
            else:
                temp.next = start2
                start2 = start2.next
            temp = temp.next


        if start1:
            temp.next = start1

        if start2:
            temp.next = start2


        return result