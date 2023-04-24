class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
    
        max_freq, left, max_length = 0, 0, 0
        
        # Iterate through the string with a right pointer
        for right in range(len(s)):
            # Update the frequency of the character at the right pointer
            count[ord(s[right]) - ord('A')] += 1
            
            # Update the maximum frequency of any character in the window
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            
            # If the number of operations required to change all other characters to the max_freq character is greater than k
            if right - left + 1 - max_freq > k:
                # Decrease the frequency of the character at the left pointer
                count[ord(s[left]) - ord('A')] -= 1
                
                # Move the left pointer to the right
                left += 1
            
            # Update the maximum length of the substring
            max_length = max(max_length, right - left + 1)
        
        return max_length

            