from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        exact_gcd = [0] * (max_val + 1)
        
        for i in range(max_val, 0, -1):
            multiples_count = 0
            for j in range(i, max_val + 1, i):
                multiples_count += freq[j]
            
            pairs_count = multiples_count * (multiples_count - 1) // 2
            
            for j in range(2 * i, max_val + 1, i):
                pairs_count -= exact_gcd[j]
                
            exact_gcd[i] = pairs_count
            
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_gcd[i]
            
        answer = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            answer.append(idx)
            
        return answer