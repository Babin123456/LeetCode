class Solution:

  def smallestPalindrome(self, s: str) -> str:
    n = len(s)
    half_len = n // 2

    first_half = sorted(s[:half_len])
    left = "".join(first_half)

    mid = s[half_len] if n % 2 == 1 else ""

    right = left[::-1]

    return left + mid + right
