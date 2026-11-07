import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = 0
        lst = []
        overall = 1
        overall_without0 = 1
        count = 0
        for i in nums:
            overall = overall * i
        for i in nums:
            if i == 0 and count < 1:
                count += 1
                continue
            else:
                overall_without0 = overall_without0 * i
        print(overall)
        print(overall_without0)
        for i in nums:
            if i != 0:
                lst.append(int(overall / i))
            else:
                lst.append(overall_without0)
        return lst
            
