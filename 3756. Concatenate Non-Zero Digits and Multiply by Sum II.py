from typing import List
import bisect
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        nz_indices = []
        nz_digits = []
        
        for i, char in enumerate(s):
            if char != '0':
                nz_indices.append(i)
                nz_digits.append(int(char))
        
        k = len(nz_digits)
        
        if k == 0:
            return [0] * len(queries)
            
        pref_sum = [0] * (k + 1)
        for i in range(k):
            pref_sum[i+1] = pref_sum[i] + nz_digits[i]
            
        pref_val = [0] * (k + 1)
        for i in range(k):
            pref_val[i+1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        ans = []
        
        for l, r in queries:
            idx_start = bisect.bisect_left(nz_indices, l)
            idx_end = bisect.bisect_right(nz_indices, r) - 1
            
            if idx_start > idx_end:
                ans.append(0)
                continue
                
            length = idx_end - idx_start + 1
            
            digit_sum = pref_sum[idx_end + 1] - pref_sum[idx_start]
            
            x = (pref_val[idx_end + 1] - pref_val[idx_start] * pow10[length]) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans