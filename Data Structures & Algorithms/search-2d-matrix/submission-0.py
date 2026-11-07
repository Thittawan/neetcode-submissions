class Solution:
    def search(self, nums: list[list[int]], target: int) -> list:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            num = nums[mid]
            if num[0] < target and num[len(num)-1] < target:
                low = mid + 1
            elif num[0] > target and num[len(num)-1] > target:
                high = mid - 1
            else:
                return nums[mid]
        return []
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        correct_lst = self.search(matrix, target)
        if len(correct_lst) == 0:
            return False
        low = 0
        high = len(correct_lst) - 1
        while low <= high:
            mid = (high + low) // 2
            num = correct_lst[mid]
            if num < target:
                low = mid + 1
            elif num > target:
                high = mid - 1
            else:
                return True
        return False