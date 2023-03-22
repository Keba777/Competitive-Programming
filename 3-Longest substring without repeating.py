class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur,prev,start = 0,0,0
        right = len(s)
        left = 0
        lookup = {}
        while left < right:
            if s[left] not in lookup:
                cur += 1
            else:
                start = max(start,lookup[s[left]])
                cur = left-start
            lookup[s[left]] = left
            prev = max(cur,prev)
            left+=1
        return prev
