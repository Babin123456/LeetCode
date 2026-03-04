class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1

        return res