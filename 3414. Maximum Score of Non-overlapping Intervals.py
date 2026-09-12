from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted([(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)])
        starts = [x[0] for x in arr]
        
        next_idx = []
        for i in range(n):
            r = arr[i][1]
            idx = bisect_left(starts, r + 1)
            next_idx.append(idx)
            
        memo = {}

        def dp(i: int, k: int):
            if k == 4 or i == n:
                return (0, [])
            
            state = (i, k)
            if state in memo:
                return memo[state]
            
            best_w, best_indices = dp(i + 1, k)
            
            nxt = next_idx[i]
            rem_w, rem_indices = dp(nxt, k + 1)
            take_w = arr[i][2] + rem_w
            take_indices = sorted([arr[i][3]] + rem_indices)
            
            if take_w > best_w:
                best_w, best_indices = take_w, take_indices
            elif take_w == best_w and take_w > 0:
                if not best_indices or take_indices < best_indices:
                    best_indices = take_indices
                    
            memo[state] = (best_w, best_indices)
            return memo[state]

        return dp(0, 0)[1]