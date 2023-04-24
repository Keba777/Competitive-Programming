class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_len = Counter(s1)
        window_len = Counter()

        for index, value in enumerate(s2):
            window_len[value] += 1

            if index >= k:
                if window_len[s2[index - k]] == 1:
                    del window_len[s2[index - k]]

                else:
                    window_len[s2[index - k]] -= 1

            if window_len == s1_len:
                return True

        return False


