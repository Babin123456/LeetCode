from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))
        
        result = [0] * n
        
        groups = []
        current_group_vals = deque()
        current_group_indices = []
        
        for i in range(n):
            val, idx = sorted_pairs[i]
            
            if current_group_vals and val - current_group_vals[-1] > limit:
                current_group_indices.sort()
                for original_idx in current_group_indices:
                    result[original_idx] = current_group_vals.popleft()
                
                current_group_indices = []
            
            current_group_vals.append(val)
            current_group_indices.append(idx)
        
        if current_group_vals:
            current_group_indices.sort()
            for original_idx in current_group_indices:
                result[original_idx] = current_group_vals.popleft()
                
        return result