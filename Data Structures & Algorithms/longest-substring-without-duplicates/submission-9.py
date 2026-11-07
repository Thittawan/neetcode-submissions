class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqe = set()
        l = 0
        r = 0
        maxx = 0
        while r < len(s):
            current = s[r]
            if current not in uniqe:
                maxx = max(maxx, r - l + 1)
                uniqe.add(current)
                r+=1
                continue
            else:
                while s[l] != current:
                    print("inside", s[l])
                    print("inside2", current)
                    uniqe.remove(s[l])
                    l+=1
                uniqe.remove(s[l])
                l+=1
        return maxx
            