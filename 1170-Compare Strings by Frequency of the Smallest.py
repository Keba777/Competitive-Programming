class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def count_min_char(word):
            return word.count(min(word))

        list1 = [count_min_char(q) for q in queries]
        list2 = [count_min_char(w) for w in words]

        list2.sort()

        result = []
        for q in list1:
            count = len(list2) - bisect.bisect(list2, q)
            result.append(count)

        return result
