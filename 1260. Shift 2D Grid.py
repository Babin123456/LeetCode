class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        if k == 0:
            return grid
            
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                curr_1d_index = r * n + c
                
                new_1d_index = (curr_1d_index + k) % total_elements
                
                new_r = new_1d_index // n
                new_c = new_1d_index % n
                
                result[new_r][new_c] = grid[r][c]
                
        return result
