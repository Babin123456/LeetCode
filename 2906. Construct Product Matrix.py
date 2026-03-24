class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        res = [[1] * m for _ in range(n)]

        p = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = p
                p = (p * grid[i][j]) % MOD

        s = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = (s * res[i][j]) % MOD
                s  = (s * grid[i][j]) % MOD

        return res       