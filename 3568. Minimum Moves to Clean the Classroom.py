from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litter_map = {}
        litter_count = 0
        
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_r, start_c = r, c
                elif cell == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        target_mask = (1 << litter_count) - 1
        
        if target_mask == 0:
            return 0
        
        max_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        queue = deque([(start_r, start_c, 0, energy, 0)])  
        max_energy[start_r][start_c][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, e, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                    
                    cell = classroom[nr][nc]
                    nmask = mask
                    
                    if cell == 'R':
                        ne = energy
                    elif cell == 'L':
                        nmask |= (1 << litter_map[(nr, nc)])
                    
                    if nmask == target_mask:
                        return steps + 1
                    
                    if ne > max_energy[nr][nc][nmask]:
                        max_energy[nr][nc][nmask] = ne
                        queue.append((nr, nc, nmask, ne, steps + 1))
                        
        return -1