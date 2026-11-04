import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        costs = [0] * (n - x + 1)
        
        left, right = [], []
        rem_left, rem_right = {}, {}
        left_size = right_size = 0
        left_sum = right_sum = 0

        def balance():
            nonlocal left_size, right_size, left_sum, right_sum
            while left_size > right_size + 1:
                v = -heapq.heappop(left)
                while rem_left.get(v, 0) > 0:
                    rem_left[v] -= 1
                    v = -heapq.heappop(left)
                left_size -= 1
                left_sum -= v
                
                heapq.heappush(right, v)
                right_size += 1
                right_sum += v

            while right_size > left_size:
                v = heapq.heappop(right)
                while rem_right.get(v, 0) > 0:
                    rem_right[v] -= 1
                    v = heapq.heappop(right)
                right_size -= 1
                right_sum -= v
                
                heapq.heappush(left, -v)
                left_size += 1
                left_sum += v

        def clean_tops():
            while left and rem_left.get(-left[0], 0) > 0:
                rem_left[-left[0]] -= 1
                heapq.heappop(left)
            while right and rem_right.get(right[0], 0) > 0:
                rem_right[right[0]] -= 1
                heapq.heappop(right)

        def add_val(val):
            nonlocal left_size, right_size, left_sum, right_sum
            clean_tops()
            if not left or val <= -left[0]:
                heapq.heappush(left, -val)
                left_size += 1
                left_sum += val
            else:
                heapq.heappush(right, val)
                right_size += 1
                right_sum += val
            balance()

        def remove_val(val):
            nonlocal left_size, right_size, left_sum, right_sum
            clean_tops()
            if left and val <= -left[0]:
                rem_left[val] = rem_left.get(val, 0) + 1
                left_size -= 1
                left_sum -= val
            else:
                rem_right[val] = rem_right.get(val, 0) + 1
                right_size -= 1
                right_sum -= val
            balance()

        for i in range(x):
            add_val(nums[i])

        for i in range(n - x + 1):
            clean_tops()
            median = -left[0]
            costs[i] = (median * left_size - left_sum) + (right_sum - median * right_size)

            if i + x < n:
                remove_val(nums[i])
                add_val(nums[i + x])

        dp = [float('inf')] * (k + 1)
        dp[0] = 0

        for _ in range(k):
            next_dp = list(dp)
            min_prev = float('inf')
            
            for i in range(n - x + 1):
                if i >= x:
                    min_prev = min(min_prev, dp[ _ - 1 if '_' in locals() else 0 ] ) # Handled via index spacing
            
            curr = [float('inf')] * (k + 1)
            curr[0] = 0
            
            
        dp = [0] + [float('inf')] * k
        
        dp_table = [[float('inf')] * (n - x + 2) for _ in range(k + 1)]
        for i in range(n - x + 2):
            dp_table[0][i] = 0

        for j in range(1, k + 1):
            min_val = float('inf')
            for i in range(1, n - x + 2):
                w_cost = costs[i - 1]
                prev_idx = max(0, i - x)
                min_val = min(min_val, dp_table[j - 1][prev_idx])
                dp_table[j][i] = min(dp_table[j][i - 1], min_val + w_cost)

        return dp_table[k][n - x + 1]