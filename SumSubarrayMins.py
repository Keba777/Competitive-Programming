class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        left = [-1] * n
        right = [n] * n

        # Calculate left
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        # Clear stack and calculate right
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        MOD = 10**9 + 7
        result = 0

        # Calculate sum of min(b)
        for i in range(n):
            result += (i - left[i]) * (right[i] - i) * arr[i]
            result %= MOD

        return result
            
