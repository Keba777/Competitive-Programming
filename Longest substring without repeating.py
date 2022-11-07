class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur,sofar,start = 0,0,0
        N = len(s)
        i = 0
        lookup = {}
        while i < N:
            if s[i] not in lookup:
                cur += 1
            else:
                start = max(start,lookup[s[i]])
                cur = i-start
            lookup[s[i]] = i
            sofar = max(cur,sofar)
            i+=1
        return sofar