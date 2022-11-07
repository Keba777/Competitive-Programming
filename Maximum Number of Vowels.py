class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        vowels_count = 0
        for i in range(k):
            if s[i] in vowels: vowels_count += 1

        l = 0
        r = k-1
        max_v = vowels_count
        while r < len(s) - 1:
            if s[l] in vowels: vowels_count -= 1
            l += 1
            r += 1
            if s[r] in vowels: vowels_count += 1
            max_v = max(max_v, vowels_count)

        return max_v