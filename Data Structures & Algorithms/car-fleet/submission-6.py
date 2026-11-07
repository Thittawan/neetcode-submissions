class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [-1]
        time = []
        for i in range(len(position)):
            time.append((target - position[i])/speed[i])
        zipped = zip(position, time)
        zipped = sorted(zipped, key=lambda tup: tup[0], reverse=True)
        print(zipped)
        for i in range(len(zipped)):
            if zipped[i][1] > stack[-1]:
                stack.append(zipped[i][1])
        return len(stack) - 1
        