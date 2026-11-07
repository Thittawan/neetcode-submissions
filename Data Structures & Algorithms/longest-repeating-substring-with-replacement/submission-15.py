class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        point1 = 0
        point2 = 0
        frequency = {}
        max_frequency = 0
        maxx = 0
        while point2 < len(s) and point1 < len(s):
            print("point1", point1)
            print("point2",point2)
            print("range", point2 - point1)
            print("max_frequency", max_frequency)
            frequency[s[point2]] = frequency.get(s[point2], 0) + 1
            max_frequency = max(max_frequency, frequency.get(s[point2]))
            while ((point2 - point1+1) - max_frequency) > k:
                frequency[s[point1]] = frequency.get(s[point1], 0) - 1
                point1 += 1
            maxx = max(maxx, point2 - point1+1)
            point2+=1
        return maxx
        