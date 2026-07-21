class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if not s:
            return 0
            
        blocks = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                blocks.append((s[i-1], count))
                count = 1
        blocks.append((s[-1], count))
        
        base_ones = sum(length for char, length in blocks if char == '1')
        
        max_delta = 0
        
        for i in range(1, len(blocks) - 1):
            if blocks[i][0] == '1':
                left_zeros = blocks[i-1][1]
                right_zeros = blocks[i+1][1]
                
                max_delta = max(max_delta, left_zeros + right_zeros)
                
        return base_ones + max_delta