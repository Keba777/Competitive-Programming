class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        for c in num:
            while k and result and result[-1] > c:
                result.pop()
                k -= 1
            result.append(c)

        while k:
            result.pop()
            k -= 1
        return "".join(result).lstrip("0") or "0"
