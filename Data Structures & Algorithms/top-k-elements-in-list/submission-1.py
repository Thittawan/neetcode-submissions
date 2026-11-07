class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        maxx = 1
        ans = []
        for i in nums:
            count = map1.get(i)
            if count is not None:
                count += 1
                map1[i] = count 
                if count > maxx:
                    maxx = count
            else:
                map1[i] = 1

        lst = [[] for _ in range(maxx+1)]
        print(maxx)
        for i in map1.keys(): 
            count = map1.get(i)
            lst[count].append(i)
        print(lst)
        index = len(lst) - 1
        while (k > 0):
            lenght = len(lst[index])
            k -= lenght
            ans.extend(lst[index])
            index = index - 1 
       
        return ans
        