class Solution:
    def minOperations(self, s: str) -> int:
        if all(c1 <= c2 for c1, c2 in zip(s, s[1:])):
            return 0
            
        n = len(s)
        if n == 2:
            return -1
            
        mid = s[1:-1]
        lo, hi = min(mid), max(mid)
        
        if s[0] <= min(lo, s[-1]) or max(s[0], hi) <= s[-1]:
            return 1
            
        if s[-1] < lo <= hi < s[0]:
            return 3
            
        return 2
