class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        
        total_cost = 0
        n = len(cost)
        
        for i in range(0, n, 3):
            total_cost += cost[i]
            
            if i + 1 < n:
                total_cost += cost[i + 1]
                
                
        return total_cost