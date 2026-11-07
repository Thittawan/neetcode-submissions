# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            if head == None:
                return False
            point1 = head
            point2 = head
            if head.next is None:
                return False
            if head.next.next is None:
                return False
            while point2 is not None:
                print(point1.val)
                print(point2.val)
                point1 = point1.next
                if point2.next is not None:
                    point2 = point2.next.next
                else:
                    point2 = point2.next
                if point1 == point2:
                    return True
            return False