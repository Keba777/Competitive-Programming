class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid
                if time > h:
                    break

            if time > h:
                left = mid + 1
            else:
                right = mid
        return left

            
