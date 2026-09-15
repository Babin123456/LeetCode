class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            found = False
            for j in range(i, n):
                if j + k <= n and s[j:j + k] == s[j:j + k][::-1]:
                    ans += 1
                    i = j + k  # Skip past this palindrome
                    found = True
                    break
                if j + k + 1 <= n and s[j:j + k + 1] == s[j:j + k + 1][::-1]:
                    ans += 1
                    i = j + k + 1  # Skip past this palindrome
                    found = True
                    break

            if not found:
                break

        return ans
