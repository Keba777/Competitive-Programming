class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(item))
        return stack[0]
