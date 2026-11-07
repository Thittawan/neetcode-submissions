class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        result = []
        for i in range(len(nums)):

            if i >= k and stack:
                if stack[0] == nums[i - k]:
                    stack.pop(0)

            while stack and nums[i] > stack[-1]:
                stack.pop()

            stack.append(nums[i])

            if i >= k-1 and stack:
                result.append(stack[0])
            
        return result


