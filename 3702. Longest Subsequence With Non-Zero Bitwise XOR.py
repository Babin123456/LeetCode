class Solution:
    def longestSubsequence(self, nums):
        xor = 0
        has_nonzero = False

        for num in nums:
            xor ^= num
            if num != 0:
                has_nonzero = True

        if xor != 0:
            return len(nums)

        if has_nonzero:
            return len(nums) - 1

        return 0
