import math 
class Solution:
    def check_time(self, piles: list[int], k: int) -> int:
        total_h = 0
        for i in piles:
            total_h += math.ceil(i / k)
        return total_h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        maxx = max(piles)
        while low <= high:
            mid = (high + low) // 2
            time = self.check_time(piles, mid)
            print("mid", mid)
            print("time", time)
            if time <= h:
                high = mid - 1
                maxx = mid  
            else:
                low = mid + 1
        return maxx

        