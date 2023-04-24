class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        n = len(p)
        anagrams = []
        target = Counter(p)
        current = Counter()

        for right in range(len(s)):
            # Add the character to the current counter
            current[s[right]] += 1

            # Remove character if the window size is larger than the pattern 'p'
            if right >= n:
                if current[s[left]] == 1:
                    del current[s[left]]
                else:
                    current[s[left]] -= 1

                left += 1

            # Compare the current counter with the target counter
            if target == current:
                anagrams.append(left)

        return anagrams
