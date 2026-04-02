class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] → max coins at (i,j) with k neutralizations used
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # start cell
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                dp[0][0][k] = 0 if k > 0 else coins[0][0]
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    
                    if i == 0 and j == 0:
                        continue
                    
                    best_prev = -float('inf')
                    
                    if i > 0:
                        best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j-1][k])
                    
                    if coins[i][j] >= 0:
                        dp[i][j][k] = best_prev + coins[i][j]
                    
                    else:
                        # option 1: take loss
                        take = best_prev + coins[i][j]
                        
                        # option 2: neutralize
                        neutral = -float('inf')
                        if k > 0:
                            prev_best = -float('inf')
                            if i > 0:
                                prev_best = max(prev_best, dp[i-1][j][k-1])
                            if j > 0:
                                prev_best = max(prev_best, dp[i][j-1][k-1])
                            neutral = prev_best
                        
                        dp[i][j][k] = max(take, neutral)
        
        return max(dp[m-1][n-1])