class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        dp[0][0] = [0, 1]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X' or (i == 0 and j == 0):
                    continue
                
                max_score = -1
                paths = 0
                
                for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n and dp[ni][nj][0] != -1:
                        prev_score, prev_paths = dp[ni][nj]
                        
                        if prev_score > max_score:
                            max_score = prev_score
                            paths = prev_paths
                        elif prev_score == max_score:
                            paths = (paths + prev_paths) % MOD
                
                if max_score != -1:
                    curr_val = 0 if board[i][j] == 'S' else int(board[i][j])
                    dp[i][j] = [max_score + curr_val, paths]
        
        res_score, res_paths = dp[n-1][n-1]
        return [res_score if res_score != -1 else 0, res_paths]