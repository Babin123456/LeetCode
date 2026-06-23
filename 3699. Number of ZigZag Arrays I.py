class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        dp0 = [1] * m
        dp1 = [1] * m
        
        for i in range(2, n + 1):
            next_dp0 = [0] * m
            next_dp1 = [0] * m
            
            pref0 = [0] * (m + 1)
            pref1 = [0] * (m + 1)
            for j in range(m):
                pref0[j + 1] = (pref0[j] + dp0[j]) % MOD
                pref1[j + 1] = (pref1[j] + dp1[j]) % MOD
            
            for y in range(m):
                next_dp0[y] = pref1[y]
                
                next_dp1[y] = (pref0[m] - pref0[y + 1] + MOD) % MOD
            
            dp0 = next_dp0
            dp1 = next_dp1
            
        total_valid = (sum(dp0) + sum(dp1)) % MOD
        return total_valid