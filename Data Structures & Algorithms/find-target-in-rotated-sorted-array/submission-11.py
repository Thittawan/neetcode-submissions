class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low  = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        while low <= high:
            mid = (high + low) // 2
            val_l = nums[low]
            val_h = nums[high]
            val_m = nums[mid]
            print("l", val_l)
            print("mid", val_m)
            print("h", val_h)
            if val_m == target:
                return mid
            if val_l <= val_m:
                if target <= val_m and target >= val_l:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= val_m and target <= val_h:
                    low = mid + 1
                else:
                    high = mid - 1

            # if val_m < target:
            #     if val_l < val_h:
            #         low = mid + 1
            #     else:
            #         high = mid - 1
            #     # if val_h >= target:
            #     #     low = mid + 1
            #     # else:
            #     #     high = mid - 1
            # else:
            #     if val_l > val_h:
            #         low = mid + 1
            #     else:
            #         high = mid - 1
            #     # if val_l <= target:
            #     #     high = mid - 1
            #     # else:
            #     #     low = mid + 1
        return -1
