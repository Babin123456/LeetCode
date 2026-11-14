class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                length = j - i + 1
                
                if length >= l and length <= r:
                    if current_sum > 0:
                        min_sum = min(min_sum, current_sum)
                elif length > r:
                    break
                    
        return min_sum if min_sum != float('inf') else -1