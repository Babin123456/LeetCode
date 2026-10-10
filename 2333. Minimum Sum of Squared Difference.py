from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        diff_counts = Counter(abs(n1 - n2) for n1, n2 in zip(nums1, nums2))
        max_diff = max(diff_counts.keys())
        
        for d in range(max_diff, 0, -1):
            if diff_counts[d] == 0:
                continue
            
            count = diff_counts[d]
            if total_k >= count:
                total_k -= count
                diff_counts[d] = 0
                diff_counts[d - 1] += count
            else:
                diff_counts[d] -= total_k
                diff_counts[d - 1] += total_k
                total_k = 0
                break
                
        if total_k > 0:
            return 0
            
        return sum(d * d * count for d, count in diff_counts.items())
