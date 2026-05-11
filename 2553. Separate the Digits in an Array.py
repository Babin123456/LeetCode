class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            for digit in str(n):
                res.append(int(digit))
        return res
