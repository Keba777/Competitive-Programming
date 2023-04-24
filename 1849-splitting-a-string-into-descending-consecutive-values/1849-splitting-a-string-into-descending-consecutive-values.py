class Solution:
    def splitString(self, s: str) -> bool:
        def isValid(s, start, prev_value, count):
            if start == len(s):
                return count >= 2
            
            curr_value = 0
            for i in range(start, len(s)):
                curr_value = curr_value * 10 + int(s[i])
                
                if (prev_value is None or prev_value - curr_value == 1) and isValid(s, i+1, curr_value, count+1):
                    return True
                    
            return False
        return isValid(s, 0, None, 0)


    