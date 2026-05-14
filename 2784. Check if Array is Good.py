class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n <= 0: return False

        counts = Counter(nums)

        for i in range(1, n):
            if counts[i] != 1:
                return False

        return counts[n] == 2