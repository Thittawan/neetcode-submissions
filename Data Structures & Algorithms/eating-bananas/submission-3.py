import math 

class Solution:

    def calculate_time(self, piles: List[int], k: int, h: int) -> bool:
        total_h = 0
        for i in piles:
            total_h += math.ceil(i/k)
        if total_h <= h:
            return True 
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = (low+high)//2
        maxx = max(piles)
        while low <= high:
            intime = self.calculate_time(piles, mid, h)
            if intime:
                maxx = min(maxx, mid)
                high = mid-1
            else:
                low = mid+1
            mid = (low+high)//2
        return maxx










            
            

        