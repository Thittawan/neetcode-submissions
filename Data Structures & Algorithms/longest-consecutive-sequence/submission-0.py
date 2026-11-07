class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        max_length = 0
        for i in range(len(nums)):
            count = 0
            current_index = 0
            while nums[i] + current_index in sets:
                current_index += 1
                count += 1
            max_length = max(max_length, count)

        return max_length
            
        