class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        all = set(nums)

        def bt(start, curr):
            if start == n:
                if not curr in all: return curr
                return ''

            for num in ('0', '1'):
                next = bt(start + 1, curr + num)
                if next: return next

        return bt(0, '')
