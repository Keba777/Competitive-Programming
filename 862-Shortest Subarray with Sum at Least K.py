class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        queue = deque()
        result = n + 1
        for i in range(n + 1):
            while queue and pre_sum[i] - pre_sum[queue[0]] >= k:
                result = min(result, i - queue.popleft())

            while queue and pre_sum[queue[-1]] >= pre_sum[i]:
                queue.pop()
            queue.append(i)

        return result if result <= n else -1
        
