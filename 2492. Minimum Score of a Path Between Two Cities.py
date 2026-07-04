class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
            
        res = float('inf')
        queue = collections.deque([1])
        visited = {1}
        
        while queue:
            u = queue.popleft()
            for v, d in adj[u]:
                res = min(res, d)
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
                    
        return res