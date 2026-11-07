class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        mid = (low + high) // 2
        mini = 1000
        while low <= high:
            val_l = nums[low]
            val_h = nums[high]
            val_m = nums[mid]
            current = min(val_l, val_h)
            current2 = min(current, val_m)
            mini = min(mini, current2)
            print("low", val_l)
            print("mid", val_m)
            print("high", val_h)
            if val_h < val_l:
                if val_m < val_l:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return mini

# if val_m < val_l and val_m < val_h:
            #     high = mid - 1   
            # elif val_m > val_l and val_m > val_h:
            #     low = mid + 1
            # else:
            #     if val_l > val_h:
            #         high = mid - 1
            #     else:
            #         if val_m > val_l:
            #             high = mid - 1
            #         else:
            #             low = mid + 1
            


        