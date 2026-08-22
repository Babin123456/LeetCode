import math
from itertools import combinations
from typing import List


class Solution:

  def findKthSmallest(self, coins: List[int], k: int) -> int:
    # Precompute LCM and sign for all non-empty subsets
    n = len(coins)
    subsets = []
    for r in range(1, n + 1):
      sign = 1 if r % 2 == 1 else -1
      for combo in combinations(coins, r):
        lcm_val = combo[0]
        for c in combo[1:]:
          lcm_val = math.lcm(lcm_val, c)
        subsets.append((lcm_val, sign))

    def count_multiples(m: int) -> int:
      total = 0
      for lcm_val, sign in subsets:
        total += sign * (m // lcm_val)
      return total

    # Binary search the answer
    left, right = 1, min(coins) * k
    ans = right

    while left <= right:
      mid = (left + right) // 2
      if count_multiples(mid) >= k:
        ans = mid
        right = mid - 1
      else:
        left = mid + 1

    return ans