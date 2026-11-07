class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [0]*(len(nums)+1)
        mapp = {}
        for i in nums:
            if mapp.get(i):
                mapp[i] += 1
            else:
                mapp[i] = 1
        for i in mapp.keys():
            fre = mapp[i]
            if lst[fre] == 0:
                lst[fre] = [i]
            else:
                lst[fre].append(i)
        result = []
        for i in range(len(lst)-1, -1, -1):
            if k <= 0:
                return result
            if lst[i] != 0:
                for j in lst[i]:
                    result.append(j)
                    k-=1
                    if k <= 0:
                        return result
        return result