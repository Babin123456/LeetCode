class Solution:

  def closedIsland(self, grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
      if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
        return
      # Mark current land as visited/water
      grid[r][c] = 1
      # Traverse all 4 directions
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

    # Step 1: Flood-fill all land cells connected to the boundary
    for r in range(rows):
      for c in range(cols):
        if (
            (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
            and grid[r][c] == 0
        ):
          dfs(r, c)

    # Step 2: Count remaining closed islands
    closed_islands_count = 0
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 0:
          closed_islands_count += 1
          dfs(r, c)  # Clear this closed island

    return closed_islands_count