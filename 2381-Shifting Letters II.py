class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        prefix_sum = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                prefix_sum[start] += 1
                prefix_sum[end + 1] -= 1

            else:
                prefix_sum[start] -= 1
                prefix_sum[end + 1] += 1

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i -1]

        ans = []
        for i, c in enumerate(s):
            current = (ord(c) - 97 + prefix_sum[i]) % 26
            ans.append(chr(current + 97))
        return "".join(ans)

