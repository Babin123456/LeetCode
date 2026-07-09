from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        current_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            
            component[i] = current_id
            
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans