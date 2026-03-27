class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        k = k % m

        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + k) % m]: return False
                else:
                    if mat[i][j] != mat[i][(j - k) % m]: return False

        return True
