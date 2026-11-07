class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        point1 = 0
        point2 = len(nums) - 1
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            point1 = 1 + i
            point2 = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while point1 < point2:
                if point1 == i:
                    point1 += 1
                    continue
                if point2 == i:
                    point2 -= 1
                    continue
                val_l = nums[point1]
                val_r = nums[point2]
                total = val_l + val_r + nums[i]
                # print("point1", val_l)
                # print("point2", val_r)
                # print("total", total)
                if total > 0:
                    point2 -= 1
                elif total < 0:
                    point1 += 1
                else:
                    ans.append([nums[i],val_l,val_r])
                    point1 += 1
                    point2 -= 1
                    while point1 < point2 and nums[point1] == nums[point1-1]:
                        point1+=1
        return ans


