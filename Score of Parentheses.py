class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for par in s:
            if par == '(':
                stack.append(0)
            elif par == ')':
                score = stack.pop()
                stack[-1] += max(2 * score, 1)
            else:
                continue
        return stack.pop()
        
            
