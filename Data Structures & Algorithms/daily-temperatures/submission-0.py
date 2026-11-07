class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        print(stack)
        result = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            print(stack)
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                print(i)
                index = stack.pop()
                diff = i - index 
                result[index] = diff
            stack.append(i)
        print(result)
        return result 
            
        
        