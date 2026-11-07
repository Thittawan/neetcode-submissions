class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if(map.get(i, -1) == -1):
                map[i] = 1
            else:
                map[i] = map.get(i) + 1
        for i in nums:
            if (map.get(i) > 1)   :
                return True
        return False     
        