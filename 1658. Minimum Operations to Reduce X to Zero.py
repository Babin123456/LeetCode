class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target_sum = sum(nums) - x
        
        if target_sum == 0:
            return len(nums)
        
        if target_sum < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target_sum and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target_sum:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1