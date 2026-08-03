class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            take_sum = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
                    max_diff = max(max_diff, take_sum - dp[k % 4])
            
            dp[0] = max_diff
            dp[1], dp[2], dp[3] = dp[0], dp[1], dp[2]

        diff = dp[1]
        
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"