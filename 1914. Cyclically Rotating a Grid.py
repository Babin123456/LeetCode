class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for l in range(min(m, n) // 2):
            r1, c1, r2, c2 = l, l, m - 1 - l, n - 1 - l

            coords = ([(r1, j) for j in range(c1, c2)] + [(i, c2) for i in range(r1, r2)] + [(r2, j) for j in range(c2, c1, -1)] + [(i, c1) for i in range(r2, r1, -1)])

            vals= [grid[r][c] for r, c in coords]
            shift = k % len(vals)
            rotated = vals[shift:] + vals[:shift]

            for (r, c), v in zip(coords, rotated):
                grid[r][c] = v
        return grid