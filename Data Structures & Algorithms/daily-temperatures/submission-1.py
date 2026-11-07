class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        result = []
        stack = [0]
        for i in temperatures:
            result.append(0)
        for i in range(len(temperatures)):
            current = temperatures[i]
            while len(stack) != 0 and current > temperatures[stack[-1]]:
                print("stack", stack)
                top_val = stack.pop()
                distance = i - top_val
                print("i", i)
                print("top", top_val)
                result[top_val] = distance
            stack.append(i)
        return result