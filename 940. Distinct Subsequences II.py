class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            last[idx] = (sum(last) + 1) % MOD
            
        return sum(last) % MOD