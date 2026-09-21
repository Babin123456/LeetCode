from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k  
        
        for num in nums:
            rem = num % k
            next_dp = [0] * k
            
            next_dp[rem] += 1
            
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * rem) % k] += dp[r]
            
            for r in range(k):
                result[r] += next_dp[r]
                
            dp = next_dp
            
        return result
