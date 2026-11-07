class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freq = {}
        maxx_freq = 0
        result = 0
        while r < len(s) and l < len(s):
            curr = s[r]
            freq[curr] = freq.get(curr, 0)+1
            maxx_freq = max(freq[curr], maxx_freq)
            while (((r - l + 1) - maxx_freq) > k):
                freq[s[l]] = freq.get(s[l], 0)-1 
                l+=1
            result = max(result, r-l+1)
            r+=1

        return result
            
