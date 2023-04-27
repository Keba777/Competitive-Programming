class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        def backtrack(combination, open_count, close_count):
            if len(combination) == 2 * n:
                temp.append(combination)
                return

            if open_count > 0:
                backtrack(combination + '(', open_count - 1, close_count)

            if close_count > 0 and close_count > open_count:
                backtrack(combination + ')', open_count, close_count - 1)

        backtrack('', n, n)
        return temp
