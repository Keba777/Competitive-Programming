class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(capacity):
            current_days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    current_days += 1
                    current_weight = 0
                current_weight += weight
            return current_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1

        return left

