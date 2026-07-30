class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        k = n // 8
        r = n % 8
        return 8 * (k * (k + 1) // 2) + r * (k + 1)