from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([(0, 0)]) 
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == n - 1:
                return steps
                
            next_indices = [idx - 1, idx + 1]
            
            if arr[idx] in graph:
                next_indices.extend(graph[arr[idx]])
                del graph[arr[idx]]
                
            for next_idx in next_indices:
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
        return -1