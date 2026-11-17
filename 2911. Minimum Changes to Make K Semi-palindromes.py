class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        def get_changes(i, j, d):
            changes = 0
            sub_len = j - i + 1
            for start in range(d):
                left = i + start
                right = i + sub_len - 1 - (start % d) 
                group_indices = []
                curr = i + start
                while curr <= j:
                    group_indices.append(curr)
                    curr += d
                
                l, r = 0, len(group_indices) - 1
                while l < r:
                    if s[group_indices[l]] != s[group_indices[r]]:
                        changes += 1
                    l += 1
                    r -= 1
            return changes

        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                sub_len = j - i + 1
                min_c = float('inf')
                for d in divisors[sub_len]:
                    min_c = min(min_c, get_changes(i, j, d))
                cost[i][j] = min_c
                
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for c in range(1, min(k, i) + 1):
                for j in range(c - 1, i):
                    if j == 0:
                        if c == 1:
                            dp[i][c] = min(dp[i][c], cost[0][i - 1])
                    else:
                        if dp[j][c - 1] != float('inf') and cost[j][i - 1] != float('inf'):
                            dp[i][c] = min(dp[i][c], dp[j][c - 1] + cost[j][i - 1])
                            
        return dp[n][k]