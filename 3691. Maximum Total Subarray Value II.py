import heapq
import math
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        K = int(math.log2(n)) + 1
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def get_val(l: int, r: int) -> int:
            length = r - l + 1
            j = int(math.log2(length))
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        max_heap = []
        for l in range(n):
            val = get_val(l, n - 1)
            heapq.heappush(max_heap, (-val, l, n - 1))
            
        total_value = 0
        
        for _ in range(k):
            neg_val, l, r = heapq.heappop(max_heap)
            total_value += (-neg_val)
            
            if r > l:
                next_val = get_val(l, r - 1)
                heapq.heappush(max_heap, (-next_val, l, r - 1))
                
        return total_value