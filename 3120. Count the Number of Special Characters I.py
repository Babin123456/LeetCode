class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set(word)
        
        count = 0
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            if lower_char in lower_set and upper_char in lower_set:
                count += 1
                
        return count