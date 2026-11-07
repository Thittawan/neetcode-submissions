class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        map = {}
        lst = []
        for i in range(len(nums)):
            diff = target - nums[i]
            print(map)
            if nums[i] in map:
                return [map.get(nums[i]), i] 
            else:
                map[diff] = i 
        

                
                
                



