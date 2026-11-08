class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_l = [1]
        prefix_r = [1]
        for i in range(len(nums)-1):
            total = prefix_l[i] * nums[i]
            prefix_l.append(total)
        
        for i in range(len(nums)-1, 0, -1):
            total = prefix_r[len(prefix_r)-1] * nums[i]
            prefix_r.append(total)
        
        ans = []
        for i in range(len(nums)):
            curr = prefix_l[i] * prefix_r[(i+1)*-1]
            ans.append(curr)

        # print(prefix_l)
        # print(prefix_r)
        # print(ans)
        return ans


        