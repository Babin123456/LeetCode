import sys
from typing import List

sys.setrecursionlimit(200_000)


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def dfs_reparent(u: int) -> None:
            ch = ord(s[u]) - 97
            prev = last_seen[ch]
            if prev != -1:
                new_parent[u] = prev

            last_seen[ch] = u
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[ch] = prev  # backtrack

        dfs_reparent(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [1] * n

        def dfs_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += dfs_size(v)
            ans[u] = total
            return total

        dfs_size(0)
        return ans