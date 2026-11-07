class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        original = set(nums)
        maxx = 0
        for i in nums:
            current = 1
            num = i
            while i+1 in original:
                if num+1 in original:
                    current += 1
                else:
                    break
                num+=1
            maxx = max(maxx, current)
            current = 1
        return maxx


