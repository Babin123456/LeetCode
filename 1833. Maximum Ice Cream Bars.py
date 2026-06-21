class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        
        frequency = [0] * (max_cost + 1)
        for cost in costs:
            frequency[cost] += 1
            
        ice_cream_count = 0
        
        for cost in range(1, max_cost + 1):
            if frequency[cost] == 0:
                continue
                
            if coins < cost:
                break
                
            count_to_buy = min(frequency[cost], coins // cost)
            
            ice_cream_count += count_to_buy
            coins -= count_to_buy * cost
            
        return ice_cream_count
