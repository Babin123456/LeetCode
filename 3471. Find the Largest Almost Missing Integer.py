from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        
        # Case 1: k == 1
        if k == 1:
            unique_elements = [x for x, count in freq.items() if count == 1]
            return max(unique_elements) if unique_elements else -1
        
        # Case 2: k == n
        if k == n:
            return max(nums)
        
        # Case 3: 1 < k < n
        ans = -1
        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])
        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
