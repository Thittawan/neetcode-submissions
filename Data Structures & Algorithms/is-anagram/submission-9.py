class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst = [0]*26
        s = s.upper()
        t = t.upper()
        for i in s:
            asc = ord(i) - 65
            lst[asc] += 1
        for i in t:
            asc = ord(i) - 65
            lst[asc] -= 1
            if lst[asc] < 0:
                return False
        return True