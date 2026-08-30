class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)

        option1 = b + 1

        option2 = n - a

        option3 = (a + 1) + (n - b)

        return min(option1, option2, option3)
