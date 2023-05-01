class Solution:
    def average(self, salary: List[int]) -> float:
        max_item = max(salary)
        min_item = min(salary)
        result = 0
        n = len(salary) - 2
        for item in salary:
            result += item
        result -= max_item
        result -= min_item
        return result / n