class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        def get_landing(r, c, d):
            curr_r, curr_r_delta = r, 0
            curr_c, curr_c_delta = c, 0
            
            if d == 0:
                curr_c_delta = 1
            else:
                curr_r_delta = 1
                
            cr, cc = curr_r + curr_r_delta, curr_c + curr_c_delta
            cd = d
            
            while 0 <= cr < m and 0 <= cc < n:
                if grid[cr][cc] == 0:
                    return (cr, cc, cd)
                if cd == 0:
                    cd = 1
                    cr += 1
                else:
                    cd = 0
                    cc += 1
            return None 

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        for d in range(2):
            landing = get_landing(0, 0, d)
            if landing:
                lr, lc, ld = landing
                dp[lr][lc][ld] = (dp[lr][lc][ld] + 1) % MOD

        for i in range(m):
            for j in range(n):
                for d in range(2):
                    ways = dp[i][j][d]
                    if ways == 0:
                        if i == 0 and j == 0:
                            continue 
                        continue
                    
                    for next_d in range(2):
                        landing = get_landing(i, j, next_d)
                        if landing:
                            lr, lc, ld = landing
                            dp[lr][lc][ld] = (dp[lr][lc][ld] + ways) % MOD

        total_paths = (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD
        return total_paths
