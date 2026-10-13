class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums, key=abs)
        
        score = 0
        mid = n // 2
        
        for i in range(mid):
            score -= sorted_nums[i] ** 2
            
        for i in range(mid, n):
            score += sorted_nums[i] ** 2
            
        return score