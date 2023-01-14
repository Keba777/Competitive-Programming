class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return int(str(b) + str(a)) - int(str(a) + str(b))

        nums = list(map(str, nums))

        nums = sorted(nums, key=functools.cmp_to_key(compare))

        return str(int(''.join(nums)))
        
