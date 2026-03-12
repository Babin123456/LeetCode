from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        parent = list(range(n))
        rank = [0]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            pa,pb = find(a),find(b)
            if pa == pb:
                return False
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa]+=1
            return True


        def can(x):

            for i in range(n):
                parent[i] = i
                rank[i] = 0

            upgrades = 0
            used = 0

            # mandatory edges must be taken
            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not union(u,v):
                        return False
                    used += 1

            normal = []
            upgrade = []

            for u,v,s,m in edges:
                if m == 0:
                    if s >= x:
                        normal.append((u,v))
                    elif s*2 >= x:
                        upgrade.append((u,v))

            # use normal edges first
            for u,v in normal:
                if union(u,v):
                    used += 1

            # then upgraded edges
            for u,v in upgrade:
                if union(u,v):
                    upgrades += 1
                    used += 1
                    if upgrades > k:
                        return False

            return used == n-1


        left, right = 0, 2*10**5
        ans = -1

        while left <= right:
            mid = (left+right)//2

            if can(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans