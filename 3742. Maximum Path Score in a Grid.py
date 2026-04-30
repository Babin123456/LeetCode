class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        
        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            
            for j in range(n):
                val = grid[i][j]
                score = val
                cost = 0 if val == 0 else 1
                
                for c in range(k + 1):
                    if c < cost:
                        continue
                    
                    best = -1
                    
                    # from top
                    if i > 0 and dp[j][c - cost] != -1:
                        best = max(best, dp[j][c - cost])
                    
                    # from left
                    if j > 0 and new_dp[j - 1][c - cost] != -1:
                        best = max(best, new_dp[j - 1][c - cost])
                    
                    # start cell
                    if i == 0 and j == 0 and c == 0:
                        best = 0
                    
                    if best != -1:
                        new_dp[j][c] = best + score
            
            dp = new_dp
        
        res = max(dp[n - 1])
        return res if res != -1 else -1