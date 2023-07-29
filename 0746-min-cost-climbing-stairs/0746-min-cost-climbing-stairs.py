class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def helper(i):
            if i <= 1:
                return cost[i]
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(helper(i-1), helper(i-2))
            return memo[i]
        
        return min(helper(n-1), helper(n-2))