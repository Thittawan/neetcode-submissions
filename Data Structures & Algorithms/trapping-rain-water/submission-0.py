class Solution:
    def trap(self, height: List[int]) -> int:
        current_max = 0
        stack = []
        count = 0
        for i in range(len(height)):
            if not stack or height[i] < height[stack[-1]]:
                stack.append(i)
                continue
            while len(stack) != 0 and height[i] >= height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                counting = min(height[stack[-1]], height[i]) - height[mid]
                print("stack", stack)
                print("counting", counting)
                print("current_max", current_max)
                count += counting * (i - stack[-1] - 1)
            stack.append(i)
        return count

            # print("stack", stack)
            # print("count", count)
            # print("current_max", current_max)
