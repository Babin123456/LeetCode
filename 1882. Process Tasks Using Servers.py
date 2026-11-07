import heapq


class Solution:

  def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
    free = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(free)

    busy = []  
    res = []
    current_time = 0

    for j, task_duration in enumerate(tasks):
      current_time = max(current_time, j)

      if not free and busy[0][0] > current_time:
        current_time = busy[0][0]

      while busy and busy[0][0] <= current_time:
        _, weight, idx = heapq.heappop(busy)
        heapq.heappush(free, (weight, idx))

      weight, idx = heapq.heappop(free)
      res.append(idx)
      heapq.heappush(busy, (current_time + task_duration, weight, idx))

    return res