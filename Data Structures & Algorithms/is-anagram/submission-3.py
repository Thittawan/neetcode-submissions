class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        count = 0
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            cha = map1.get(s[i], -1)
            cha2 = map2.get(t[i], -1)
            if cha == -1:
                map1[s[i]] = 1
            else:
                map1[s[i]] += 1
            if cha2 == -1:
                map2[t[i]] = 1
            else:
                map2[t[i]] += 1
        if map1 == map2:
            return True
        else: 
            return False

        