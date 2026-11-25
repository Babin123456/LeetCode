from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod = (1 << 61) - 1
        base = 1315423911

        pow_base = [1] * (n + 1)
        pref_hash = [0] * (n + 1)

        for i in range(n):
            pow_base[i + 1] = (pow_base[i] * base) % mod
            pref_hash[i + 1] = (pref_hash[i] * base + nums[i]) % mod

        def has_unique_of_length(length: int) -> bool:
            if length == n:
                return True
            seen = Counter()
            weight = pow_base[length]
            for start in range(n - length + 1):
                end = start + length
                h = (pref_hash[end] - pref_hash[start] * weight) % mod
                seen[h] += 1
            return any(count == 1 for count in seen.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans