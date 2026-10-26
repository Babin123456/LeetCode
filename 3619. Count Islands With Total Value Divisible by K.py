from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        valid_islands = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    # Start BFS/DFS for a new island
                    current_sum = 0
                    queue = deque([(r, c)])
                    current_sum += grid[r][c]
                    grid[r][c] = 0  # Mark as visited
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                current_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                    
                    # Check divisibility condition
                    if current_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands