import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        point1 = 0
        point2 = 0
        total = len(nums1) + len(nums2)
        mid = total // 2
        position = 0
        prev = 0
        curr = 0
        while position <= mid:
            prev = curr
            if point1 < len(nums1) and (point2 >= len(nums2) or nums1[point1] < nums2[point2]):
                curr = nums1[point1]
                point1+=1
                position+=1
            else:
                curr = nums2[point2]
                point2+=1
                position+=1
        if total % 2 == 0:
            val = (prev + curr) / 2
            return val
        else:
            return curr
        
            




