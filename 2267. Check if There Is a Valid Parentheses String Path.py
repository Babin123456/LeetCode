from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        max_k = (m + n) // 2

        @lru_cache(None)
        def dfs(r: int, c: int, k: int) -> bool:
            if grid[r][c] == '(':
                k += 1
            else:
                k -= 1
            
            if k < 0 or k > max_k:
                return False
            
            if r == m - 1 and c == n - 1:
                return k == 0
            
            if r + 1 < m and dfs(r + 1, c, k):
                return True
            if c + 1 < n and dfs(r, c + 1, k):
                return True
            
            return False

        return dfs(0, 0, 0)