class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        mapp = {}
        for i in nums:
            if i not in nums_set:
                continue
            # if mapp.get(i+1):
            #     mapp[i] = mapp.get(i+1) + 1
            # else:
            total = 1
            temp = i+1
            nums_set.remove(i)
            while temp in nums_set:
                # print(temp)
                nums_set.remove(temp)
                temp += 1
                total += 1
            # print(temp)
            if mapp.get(temp):
                    mapp[i] = mapp.get(temp) + total
            else:
                mapp[i] = total
            # print(mapp)



        longest = 0
        for i in mapp.keys():
            if mapp[i] > longest:
                longest = mapp[i]
        return longest