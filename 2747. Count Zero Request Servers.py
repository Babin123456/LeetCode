class Solution:

  def countServers(
      self, n: int, logs: List[List[int]], x: int, queries: List[int]
  ) -> List[int]:
    logs.sort(key=lambda x: x[1])

    indexed_queries = sorted(
        [(q, i) for i, q in enumerate(queries)], key=lambda x: x[0]
    )

    res = [0] * len(queries)
    server_count = {}
    l = 0
    r = 0
    m = len(logs)

    for q, original_idx in indexed_queries:
      window_start = q - x
      window_end = q

      while r < m and logs[r][1] <= window_end:
        server_id = logs[r][0]
        server_count[server_id] = server_count.get(server_id, 0) + 1
        r += 1

      while l < m and logs[l][1] < window_start:
        server_id = logs[l][0]
        server_count[server_id] -= 1
        if server_count[server_id] == 0:
          del server_count[server_id]
        l += 1

      res[original_idx] = n - len(server_count)

    return res