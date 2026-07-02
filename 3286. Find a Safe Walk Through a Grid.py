from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = grid[0][0]
        
        queue = deque([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost[r][c] + grid[nr][nc]
                    
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                       
                        else:
                            queue.append((nr, nc))
                            
        return health - cost[m-1][n-1] >= 1