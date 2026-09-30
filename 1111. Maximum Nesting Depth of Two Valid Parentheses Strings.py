class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        return [i & 1 if c == '(' else (i + 1) & 1 for i, c in enumerate(seq)]
