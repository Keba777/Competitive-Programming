class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverser(left, right, s):
            #Base case
            if left >= right:
                return

            #recursive relation
            s[left], s[right] = s[right], s[left]
            reverser(left+1, right-1, s)
        
        reverser(0, len(s)-1, s)
