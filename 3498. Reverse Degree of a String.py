class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(i * (26 - (ord(char) - ord('a'))) for i, char in enumerate(s, 1))