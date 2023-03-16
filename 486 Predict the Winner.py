class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.canPlayer1WinHelper(nums, 0, len(nums) - 1, 0, True)

    # create the canPlayer1Win helper function
    def canPlayer1WinHelper(self, nums, left, right, p1Score, isP1Turn):
        if left > right:
            # game is over, return True if player 1 has more points, else False
            return p1Score >= (sum(nums) - p1Score)
        
        if isP1Turn:
            # Player 1's turn
            return self.canPlayer1WinHelper(nums, left+1, right, p1Score+nums[left], False) or self.canPlayer1WinHelper(nums, left, right-1, p1Score+nums[right], False)
        else:
            # Player 2's turn
            return self.canPlayer1WinHelper(nums, left+1, right, p1Score, True) and self.canPlayer1WinHelper(nums, left, right-1, p1Score, True)

            


