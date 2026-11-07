class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = len(numbers)-1
        while point1 < point2:
            val = numbers[point1] + numbers[point2]    
            if val < target:
                point1+=1
            elif val > target:
                point2-=1
            else:
                return [point1+1, point2+1]        
        return []