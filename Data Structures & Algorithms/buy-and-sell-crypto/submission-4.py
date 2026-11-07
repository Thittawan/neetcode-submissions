class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        point1 = 0
        point2 = 1
        max_length = 0
        while point2 < len(prices):
            if prices[point1] <= prices[point2]:
                max_length = max(max_length, prices[point2] - prices[point1])
            else:
                point1 = point2
            point2 += 1
        return max_length
        