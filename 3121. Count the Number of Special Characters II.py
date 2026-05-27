class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        invalidated = set()
        
        for i, char in enumerate(word):
            if char.islower():
                if char.isupper() or char.upper() in first_upper:
                    invalidated.add(char)
                last_lower[char] = i
            else:
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        for lower_char, lower_idx in last_lower.items():
            upper_char = lower_char.upper()
            
            if upper_char in first_upper and lower_char not in invalidated:
                if lower_idx < first_upper[upper_char]:
                    special_count += 1
                    
        return special_count