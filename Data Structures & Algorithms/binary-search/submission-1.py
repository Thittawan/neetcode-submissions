class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            num = nums[mid]
            # print(num)
            if num < target:
                low = mid + 1
                # mid = (high + mid) // 2
            elif num > target:
                high = mid - 1
                # mid = (mid + low) // 2
            else:
                return mid
        return -1

        