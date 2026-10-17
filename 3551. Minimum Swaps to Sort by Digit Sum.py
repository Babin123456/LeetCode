class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            return sum(int(digit) for digit in str(n))
        
        n = len(nums)
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((get_digit_sum(val), val, i))
            
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
                
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps