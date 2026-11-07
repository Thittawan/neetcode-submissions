class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        res = [1] * n
        print(pref)
        print(suff)
        print(res)
        current = 1
        for i in range(1, n):
            current *= nums[i-1]
            pref[i] = current 
        current = 1
        for i in range(1, n):
            current *= nums[-i]
            suff[-i-1] = current 
        for i in range(n):
            res[i] = pref[i] * suff[i]
        print(pref)
        print(suff)
        print(res)
        return res
        