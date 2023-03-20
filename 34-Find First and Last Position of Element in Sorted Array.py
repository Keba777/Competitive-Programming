class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_index = mid - 1
                right_index = mid + 1
                while left_index >= 0 and nums[left_index] == target:
                    left_index -= 1
                
                while right_index < len(nums) and nums[right_index] == target:
                    right_index += 1

                return [left_index + 1, right_index - 1]
                
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]
