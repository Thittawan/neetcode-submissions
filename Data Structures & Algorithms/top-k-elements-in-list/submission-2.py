class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = {}
        maxx = 0
        for i in nums:
            val = counting.get(i, 0) + 1
            maxx = max(maxx, val)
            counting[i] = val
        lst = [] 
        for i in range(maxx):
            lst.append(set())
        print(counting)
        print(lst)
        for key in counting:
            val = counting.get(key)
            print(val)
            lst[val-1].add(key)
        final = []
        for i in range(1, len(lst) + 1):
            if k == 0:
                return final
            for j in lst[-i]:
                final.append(j)
                k-=1
                if k==0:
                    return final
        return final
        