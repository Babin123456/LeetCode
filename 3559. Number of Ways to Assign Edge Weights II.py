from collections import defaultdict
import sys

sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
                    
        dfs(1, 1, 0)
        
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u  
                
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[lca]
            
            ans.append(pow2[k - 1])
            
        return ans
