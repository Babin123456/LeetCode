class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(T, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1  
            base = T
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T = [[0] * size for _ in range(size)]
        
        for y in range(m):
            for x in range(y):
                T[y][x + m] = 1
                
            for x in range(y + 1, m):
                T[y + m][x] = 1
                
        T_pow = power(T, n - 1)
        
        total_valid = 0
        for i in range(size):
            row_sum = sum(T_pow[i]) % MOD
            total_valid = (total_valid + row_sum) % MOD
            
        return total_valid