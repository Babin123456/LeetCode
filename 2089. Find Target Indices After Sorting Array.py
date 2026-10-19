class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        left = sum(x < target for x in nums)
        right = sum(x <= target for x in nums)
        
        return list(range(left, right))