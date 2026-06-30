class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        last = {'a': -1, 'b': -1, 'c': -1}
        for i, char in enumerate(s):
            last[char] = i
            res += min(last.values()) + 1
        return res