class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        r = 0 
        fre = {}
        total = len(t)
        ans = (float('inf'),[0,0])

        for i in t: 
            val = fre.get(i, 0) + 1
            fre[i] = val

        while r < len(s):
            val = fre.get(s[r], -1)
            if s[r] in fre:
                if val > 0:
                    total-=1
                fre[s[r]] = val-1     
            while total == 0:
                new_range = r - l + 1
                if (new_range < ans[0]):
                    ans = (new_range, [l, r])
                if s[l] in fre:
                    fre[s[l]] = fre.get(s[l])+1
                    if fre[s[l]] > 0:
                        total+=1
                l += 1
            r+=1
        if ans[0] == float('inf') and ans[1] == [0,0]:
            return ""
        return s[ans[1][0] : ans[1][1]+1]
                
                




            

