class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(num, path):
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            if not num and len(path) >= 3:
                return True
            for i in range(1, len(num) + 1):
                if i > 1 and num[0] == "0":  # Leading zeros are not allowed
                    continue
                if dfs(num[i:], path + [int(num[:i])]):
                    return True
            return False

        return dfs(num, [])