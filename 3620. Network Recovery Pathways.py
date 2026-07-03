from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        max_edge = 0
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                max_edge = max(max_edge, cost)
                
        queue = deque([i for i in range(n) if in_degree[i] == 0 and online[i]])
        topo_order = []
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        def is_valid_score(min_w: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] != float('inf'):
                    for v, cost in adj[u]:
                        if cost >= min_w:
                            if dist[u] + cost < dist[v]:
                                dist[v] = dist[u] + cost
                                
            return dist[n-1] <= k

        low, high = 0, max_edge
        best_score = -1
        
        while low <= high:
            mid = (low + high) // 2
            if is_valid_score(mid):
                best_score = mid
                low = mid + 1  
            else:
                high = mid - 1 
                
        return best_score
