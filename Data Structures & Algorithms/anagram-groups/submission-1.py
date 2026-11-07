class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1  
            count = tuple(count)
            gt = map.get(count, 0) 
            if gt == 0:
                map[count] = [i]   
            else:
                map[count].append(i)
        print(map)
        result = []
        for k in map:
            lst = map.get(k)
            print(lst)
            result.append(lst)
        print(result)
        
        return result


                


        



        