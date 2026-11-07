class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # point1 = 0
        # point2 = 0
        # max_lenght = 0
        # unique = set()
        # while point2 < len(s):
        #     print(unique)
        #     print(s[point2])
        #     if s[point2] in unique:
        #         print(s[point2])
        #         if len(unique) > max_lenght:
        #             max_lenght = len(unique)
        #             point1 += 1
        #             unique.clear()
        #             unique.add(s[point1])
        #             unique.add(s[point2])
        #     else:
        #         unique.add(s[point2])
        #     point2 += 1
        # return max(max_lenght, len(unique))
        point1 = 0
        point2 = 0
        max_lenght = 0
        unique = set()
        while point2 < len(s):
            print(unique)
            print("point1", [point1])
            print("point2", [point2])
            if s[point2] in unique:
                print("point2", s[point2])
                max_lenght = max(max_lenght, point2 - point1)
                print("max_lenght", max_lenght)
                while s[point1] != s[point2]:
                    point1 += 1
                point1 += 1
                point2 = point1
                unique.clear()
                unique.add(s[point1])
                unique.add(s[point2])
            else:
                unique.add(s[point2])
            point2 += 1
        return max(max_lenght, point2 - point1)


        