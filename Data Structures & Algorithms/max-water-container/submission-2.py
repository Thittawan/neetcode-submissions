class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_point = 0
        r_point = len(heights) - 1
        most_water = -1
        while r_point > l_point:
            height = min(heights[l_point], heights[r_point])
            area = height * (r_point - l_point)
            if area >= most_water:
                most_water = area
            if heights[l_point] > heights[r_point]:
                r_point -= 1
            else:
                l_point += 1
        return most_water



        