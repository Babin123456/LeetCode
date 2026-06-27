from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        count_ones = freq.get(1, 0)
        res = count_ones - 1 if count_ones % 2 == 0 else count_ones
        res = max(res, 1) 
        
        for x in freq:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while freq.get(curr, 0) >= 2:
                current_len += 2
                curr = curr * curr
                
            if freq.get(curr, 0) >= 1:
                current_len += 1
            else:
                current_len -= 1
                
            res = max(res, current_len)
            
        return res
