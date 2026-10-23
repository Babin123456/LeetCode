class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Check if already sorted
        if all(nums[i] == i for i in range(len(nums))):
            return 0
            
        k = -1
        for i, val in enumerate(nums):
            if val != i:
                if k == -1:
                    k = val
                else:
                    k &= val
                    
        return k