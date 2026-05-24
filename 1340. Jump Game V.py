from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def dfs(i: int) -> int:
            max_visited = 1
            
            for r in range(i + 1, min(i + d + 1, n)):
                if arr[r] >= arr[i]:
                    break  
                max_visited = max(max_visited, 1 + dfs(r))
                
            for l in range(i - 1, max(-1, i - d - 1), -1):
                if arr[l] >= arr[i]:
                    break  
                max_visited = max(max_visited, 1 + dfs(l))
                
            return max_visited

        return max(dfs(i) for i in range(n))
