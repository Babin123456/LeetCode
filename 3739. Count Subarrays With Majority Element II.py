class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        bit_size = 2 * n + 2
        bit = [0] * bit_size

        def update(idx: int, val: int):
            while idx < bit_size:
                bit[idx] += val
                idx += idx & -idx

        def query(idx: int) -> int:
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & -idx
            return total

        offset = n + 1
        
        update(0 + offset, 1)
        
        total_subarrays = 0
        current_prefix_sum = 0
        
        for num in nums:
            current_prefix_sum += 1 if num == target else -1
            
            total_subarrays += query(current_prefix_sum - 1 + offset)
            
            update(current_prefix_sum + offset, 1)
            
        return total_subarrays
