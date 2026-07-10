class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nodes = sorted(list(enumerate(nums)), key=lambda x: x[1])
        
        pos = [0] * n
        for i in range(n):
            pos[nodes[i][0]] = i
            
        up = [[i] * 18 for i in range(n)] 
        
        r = 0
        for l in range(n):
            while r < n and nodes[r][1] - nodes[l][1] <= maxDiff:
                r += 1
            up[l][0] = r - 1
            
        for j in range(1, 18):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_distance(u_sorted, v_sorted):
            if u_sorted == v_sorted:
                return 0
            
            if u_sorted > v_sorted:
                u_sorted, v_sorted = v_sorted, u_sorted
                
            if up[u_sorted][17] < v_sorted:
                return -1
                
            ans = 0
            curr = u_sorted
            for j in range(17, -1, -1):
                if up[curr][j] < v_sorted:
                    curr = up[curr][j]
                    ans += (1 << j)
            
            ans += 1
            return ans

        res = []
        for u, v in queries:
            res.append(get_distance(pos[u], pos[v]))
            
        return res