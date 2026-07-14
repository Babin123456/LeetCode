import math
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def solve(idx, g1, g2):
            if idx == n:
                return 1 if (g1 > 0 and g2 > 0 and g1 == g2) else 0
            
            res = solve(idx + 1, g1, g2)
            
            next_g1 = nums[idx] if g1 == 0 else math.gcd(g1, nums[idx])
            res = (res + solve(idx + 1, next_g1, g2)) % MOD
            
            next_g2 = nums[idx] if g2 == 0 else math.gcd(g2, nums[idx])
            res = (res + solve(idx + 1, g1, next_g2)) % MOD
            
            return res
        
        return solve(0, 0, 0)
