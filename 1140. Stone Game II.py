from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dp(i: int, m: int) -> int:
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            min_opponent_score = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent_score = min(min_opponent_score, dp(i + x, max(m, x)))
                
            return suffix_sum[i] - min_opponent_score

        return dp(0, 1)
