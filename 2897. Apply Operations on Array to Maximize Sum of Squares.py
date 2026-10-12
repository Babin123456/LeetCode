class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    bit_counts[b] += 1
                    
        final_nums = [0] * k
        for i in range(k):
            current_val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    current_val |= (1 << b)
                    bit_counts[b] -= 1
            final_nums[i] = current_val
            
        total_sum = sum(x * x for x in final_nums) % MOD
        return total_sum
