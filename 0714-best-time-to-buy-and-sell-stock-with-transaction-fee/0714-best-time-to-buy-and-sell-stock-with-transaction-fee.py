class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        # Initialize the variables for holding the maximum profit
        cash = 0
        hold = -prices[0]
        
        for i in range(1, n):
            # Calculate the maximum profit if we sell the stock on the current day
            cash = max(cash, hold + prices[i] - fee)
            
            # Calculate the maximum profit if we hold the stock on the current day
            hold = max(hold, cash - prices[i])
        
        # Return the maximum profit after considering all the days
        return cash
