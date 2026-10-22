class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        target = list(range(n))
        
        def get_shift(arr):
            extended = arr + arr
            target_tuple = tuple(target)
            for i in range(n):
                if tuple(extended[i : i + n]) == target_tuple:
                    return i
            return float('inf')

        min_ops = float('inf')
        
        shift = get_shift(nums)
        if shift != float('inf'):
            min_ops = min(min_ops, shift)
            
        rev_nums = nums[::-1]
        shift = get_shift(rev_nums)
        if shift != float('inf'):
            min_ops = min(min_ops, 1 + shift)
            
        for i in range(n):
            rotated = nums[i:] + nums[:i]
            if rotated[::-1] == target:
                min_ops = min(min_ops, i + 1)
                
        for i in range(n):
            rotated = nums[i:] + nums[:i]
            rev_rotated = rotated[::-1]
            shift2 = get_shift(rev_rotated)
            if shift2 != float('inf'):
                min_ops = min(min_ops, i + 1 + shift2)
                
        return min_ops if min_ops != float('inf') else -1
