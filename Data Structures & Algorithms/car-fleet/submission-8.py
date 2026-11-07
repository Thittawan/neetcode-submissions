import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        count = 0
        for i in range(len(position)):
            val = ((target - position[i]) / speed[i])
            stack.append((position[i],val))
        print(stack)
        stack.sort(key=lambda item: item[0])
        print(stack)
        top = (0,0)
        while len(stack) != 0:
            print(top)
            current = stack.pop()
            if current[1] > top[1]:
                count+=1
                top = current
        
        print(count)
        return count


        